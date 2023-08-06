import os
import subprocess
import sys
from subprocess import Popen

import requests

try:
    import dotenv
    dotenv.load_dotenv()
except ImportError:
    pass


DEFAULT_OPTIONS = {
    'dry_run': False,
    'git_dir': None,
    'tag': None
}


class GitHubRelease:
    _previous_tag = None
    repo = owner = tag = tag_commit = github_api_key = None

    def __init__(self, options=None):
        """
        Init with some env vars or arguments
        Ref: https://circleci.com/docs/2.0/env-vars/#built-in-environment-variables
        """
        self.options = DEFAULT_OPTIONS
        if options:
            if not isinstance(options, dict):
                options = vars(options)
            self.options.update(options)
            self.tag = self.options['tag']
        self._set_env_vars()

    def _run_cmd(self, cmd, default=None):
        p = Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=os.environ)
        out, err = p.communicate()
        if p.returncode:
            return default
        return out.decode('utf8').strip()

    def _set_env_vars(self):
        env_vars = {
            'repo': 'CIRCLE_PROJECT_REPONAME',
            'owner': 'CIRCLE_PROJECT_USERNAME',
            'tag': 'CIRCLE_TAG',
            'github_api_key': 'GITHUB_API_KEY'
        }
        missing_attrs = []
        for attr, env_var in env_vars.items():
            if getattr(self, attr) is not None:
                continue  # Do not override
            env_var_value = os.getenv(env_var)
            setattr(self, attr, env_var_value)
            if env_var_value is None:
                missing_attrs.append(env_var)
        if missing_attrs:
            print('Missing attributes from environment:\n- {}'.format('\n- '.join(missing_attrs)))
            sys.exit(1)

    def _git_cmd(self, args):
        cmd = ['git']
        if self.options['git_dir']:
            cmd.append('--git-dir={}'.format(self.options['git_dir']))
        return cmd + args

    @property
    def previous_tag(self):
        if self._previous_tag:
            return self._previous_tag

        cmd = self._git_cmd(['describe', '--abbrev=0', '--tags', '{}^'.format(self.tag)])
        self._previous_tag = self._run_cmd(cmd)

        return self._previous_tag

    def _tag_commit(self, tag):
        return self._run_cmd(self._git_cmd(['rev-parse', tag]))

    def _initial_commit(self):
        return self._run_cmd(self._git_cmd(['rev-list', '--max-parents=0', 'HEAD']))

    def branches_since_previous_tag(self):
        if self.previous_tag is None:
            print('No previous tag found, assuming first tag and basing off initial commit')
            start_ref = 'Initial commit'
            start_commit = self._initial_commit()
        else:
            start_ref = self.previous_tag
            start_commit = self._tag_commit(self.previous_tag)

        refs_range = '{}...{}'.format(start_commit, self.tag_commit)
        print('Finding merges in range {} ({}...{})'.format(refs_range, start_ref, self.tag))
        out = self._run_cmd(self._git_cmd(['log', '--merges', '--pretty=format:%H;%s', refs_range]))
        if not out:
            return []
        branches = []
        for log in out.split('\n'):
            oid, merge = log.split(';')
            if not merge.startswith('Merge pull request'):
                continue

            branch = merge.split(' ')[-1]
            owner_prefix = '{}/'.format(self.owner)
            if branch.startswith(owner_prefix):
                branches.append(branch[len(owner_prefix):])
        return branches

    def format_release_body(self, pull_requests):
        """ Format a release changelog in markdown """
        if pull_requests:
            pull_requests = self._flatten_prs(pull_requests)

            pr_lines = []
            for pr in pull_requests:
                author = "@{}".format(pr['author']['login'])
                merge_commit = pr['mergeCommit']['abbreviatedOid']
                pr_lines.append("- #{} {} (by {} in {})".format(pr['number'], pr['title'], author, merge_commit))

            body = '\n'.join(pr_lines)
        else:
            body = 'No merged pull requests.'
        if self.previous_tag:
            url = 'https://github.com/{}/{}/releases/tag/{}'.format(self.owner, self.repo, self.previous_tag)
            since = 'Since [{}]({})\n'.format(self.previous_tag, url)
        else:
            since = 'Since *first commit*\n'
        return '## Changelog\n{}{}'.format(since, body)

    def _flatten_prs(self, pull_requests):
        pull_requests = map(lambda x: x[1]['edges'], pull_requests.items())
        flattened = []
        for edges in pull_requests:
            for edge in edges:
                flattened.append(edge['node'])
        return flattened

    def fetch_pull_requests(self, branches):
        headers = {"Authorization": "Bearer {}".format(self.github_api_key)}
        assert branches

        query = self._repository_query(branches)
        github_api_url = 'https://api.github.com/graphql'
        request = requests.post(github_api_url, json={'query': query}, headers=headers)
        if request.status_code == 200:
            data = request.json()

            if 'errors' in data:
                print('query', query, 'errors', data)
                return []
            return data['data']['repository']

        return []

    def _repository_query(self, branches):
        pr_queries = []
        pr_query_template = """
        pr%s: pullRequests(headRefName: "%s", first:100) {
          edges {
            node {
              headRefName
              number
              title
              author {
                login
              }
              mergeCommit {
                abbreviatedOid
              }
            }
          }
        }"""
        for i, branch in enumerate(branches):
            pr_queries.append(pr_query_template % (i, branch))
        query = """{
          repository(owner: "%s", name: "%s") {
            %s
          }
        }""" % (self.owner, self.repo, '\n'.join(pr_queries))
        return query

    def _release_data(self, tag_name, body, target_commitish='master', draft=False, prerelease=False):
        """Ref: https://developer.github.com/v3/repos/releases/#create-a-release"""
        return {
              "tag_name": tag_name,
              "target_commitish": target_commitish,
              "name": tag_name,
              "body": body,
              "draft": draft,
              "prerelease": prerelease
        }

    def create_release(self, body):
        """ Create a release tied to a tag on GitHub """
        data = self._release_data(self.tag, body)

        headers = {"Authorization": "Bearer {}".format(self.github_api_key)}
        url = 'https://api.github.com/repos/{}/{}/releases'.format(self.owner, self.repo)
        request = requests.post(url, json=data, headers=headers)
        if request.status_code == 201:
            return True

        print('Create release failed:', request.status_code, request.text)
        return False

    def _set_and_verify_tag_commit(self):
        self.tag_commit = self._tag_commit(self.tag)
        if self.tag_commit is None:
            print('Error: Tag \'{}\' not found in git index'.format(self.tag))
            sys.exit(1)

    def create_release_from_tag(self):
        self._set_and_verify_tag_commit()

        branches = self.branches_since_previous_tag()
        if not branches:
            print('No branches found')

        pull_requests = []
        if branches:
            pull_requests = self.fetch_pull_requests(branches)
            if not pull_requests:
                print("No pull requests found!")

        body = self.format_release_body(pull_requests)
        if not self.options.get('dry_run'):
            self.create_release(body)
