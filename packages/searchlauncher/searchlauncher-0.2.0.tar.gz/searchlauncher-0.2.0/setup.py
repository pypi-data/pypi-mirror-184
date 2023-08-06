# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['searchlauncher']

package_data = \
{'': ['*'], 'searchlauncher': ['settings/*']}

install_requires = \
['keyboard>=0.13.5,<0.14.0',
 'loguru>=0.6.0,<0.7.0',
 'pydantic>=1.10.4,<2.0.0',
 'tomlkit>=0.11.6,<0.12.0',
 'typer[all]>=0.7.0,<0.8.0']

extras_require = \
{':python_version < "3.11"': ['backports.strenum>=1.1.1,<2.0.0']}

entry_points = \
{'console_scripts': ['searchlauncher = searchlauncher.cli:cli']}

setup_kwargs = {
    'name': 'searchlauncher',
    'version': '0.2.0',
    'description': 'Search multiple websites using a single shortcut.',
    'long_description': '# searchlauncher\n\nSearch multiple websites at once using your default browser.\n\nThe search (launcher) can be triggered from anywhere as it\'s listening for a global keypress.\n\n### Installation\n\n```bash\npip install searchlauncher\n```\n\n#### Requirements\n\nPython `>=3.10` with [`tkinter`](https://docs.python.org/3/library/tkinter.html) installed.\n\n### Running in background\n\n```bash\nsearchlauncher\n```\n\nto start as a daemon waiting for a [configurable](#settings-and-supported-websites) keypress (e.g., `Ctrl + Shift + E`).\n\nThen type your query and press `Enter` to submit or `Esc` to close the window.\n\nThis will open the search for each website in a new tab.\n\nSearching different website groups can be triggered with different hotkeys.\n\n### Searching from console\n\nInstead of running in background, you can use the CLI run a one-off search.\n\nTo open a search for all [configured websites](#settings-and-supported-websites):\n\n```shell\nsearchlauncher search "an item I\'m looking for"\n```\n\nYou can also select a [custom search group](#settings-and-supported-websites):\n\n```shell\nsearchlauncher search "and now for something completely different" -g en\n```\n\n### Settings and supported websites\n\nTo open the config file location, you can run\n\n```shell\nsearchlauncher config\n```\n\nafter installing.\n\nSee the available [`default websites and groups`](src/searchlauncher/settings/default.toml).\n\nYou can easily modify this file to add and modify target websites as well as their groups.\n\nYou can also customise the default `shortcut` hotkey as well as shortcuts for all groups.\n\n## TODO\n\n- [x] CLI to search for a single item\n- [x] GUI (popup on hotkey)\n- Configurability\n    - [x] Customise the hotkey(s)\n    - [x] Customise search sites\n    - [x] Customisable search groups\n    - [ ] Add and select different browsers\n\n## Development\n\n### Setup\n\n1. [Install poetry](https://python-poetry.org/docs/#installation) and `cd` to this folder.\n\n2. `poetry install`\n\n3. `poetry run pre-commit install`\n',
    'author': 'Mikuláš Zelinka',
    'author_email': 'mikulas@zelinka.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MikulasZelinka/searchlauncher',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
