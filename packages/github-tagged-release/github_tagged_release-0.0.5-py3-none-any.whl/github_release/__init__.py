from __future__ import absolute_import
from argparse import ArgumentParser

__version__ = VERSION = "0.0.5"

from .github_release import GitHubRelease


def main():
    # FIXME: click
    parser = ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', dest='dry_run', help='skip creating the GitHub release')
    parser.add_argument('--tag', dest='tag', help='override the git tag (default: value of CIRCLE_TAG env var)')
    parser.add_argument('--git-dir', dest='git_dir', help='override GIT_DIR (default: \'.\')')
    parser.add_argument('--version', action='version', version=VERSION)
    options = parser.parse_args()
    GitHubRelease(options).create_release_from_tag()


if __name__ == '__main__':
    main()
