# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitea_github_sync']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'piny>=0.6.0,<0.7.0',
 'pydantic>=1.10.4,<2.0.0',
 'pygithub>=1.57,<2.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=13.0.0,<14.0.0']

entry_points = \
{'console_scripts': ['gitea-github-sync = gitea_github_sync.cli:cli']}

setup_kwargs = {
    'name': 'gitea-github-sync',
    'version': '0.1.0',
    'description': 'Syncs your gitea instance with your Github account',
    'long_description': '# gitea-github-sync\n\ngitea-github-sync provides a simple CLI to sync Github repositories to your Gitea instance.\n\n## Installation\n\n```\npip install gitea-github-sync\n```\n\n## Setup\nCreate a file in `$HOME/.config/gitea-github-sync/config.yml` with the following template and fill up the missing values:\n\n```yaml\ngitea_api_url: https://<your-gitea-instance>/api/v1\ngitea_token: <your-gitea-token>\ngithub_token: <your-github-token>\n```\n\n### Creating a Gitea token\nGo to https://\\<your-local-gitea-instance\\>/user/settings/applications and generate a new token.\n\n### Creating a Github token\n\nGo to https://github.com/settings/tokens/new and create a token with the following values set:\n- Note: this is a note to help you understand how the token is used.\n- Expiration: No expiration\n- repo: Select all of repo\n\n![Screenshot of token configuration](docs/readme/github_token_permission.png)\n\n#### Github token limitation\nGithub allows you to create _Personal access tokens_. These tokens now exist in two different flavors:\n- Fine-grained tokens\n- Classic tokens\n\nBoth work with gitea-github-sync, but given that Gitea does not allow the modification of the access token through the API, a **non-expiring** token must be used which limits the usage to Classic tokens.\n\n## Usage\n\n`gitea-github-sync --help` Shows the help\n\n`gitea-github-sync list-all-gitea-repositories` Lists all available Gitea repositories in your account\n\n`gitea-github-sync list-all-github-repositories` Lists all available Github repositories in your account\n\n`gitea-github-sync migrate-repo FULL_REPO_NAME` Migrates one repo from Github to Gitea\n`\n`gitea-github-sync sync` Migrates all repos not present in Gitea from Github\n\n## Limitations\n\nWhen using the migration feature of Gitea, a Github token must be passed for Gitea to continuously pull the new changes from Github.\n\nThe token used by gitea-github-sync to list repositories is the same that is used by Gitea for continuous monitoring. Updating the value of this token is unfortunately not possible through the API as of now. \n',
    'author': 'Kevin Grandjean',
    'author_email': 'Muscaw@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Muscaw/gitea-github-sync',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
