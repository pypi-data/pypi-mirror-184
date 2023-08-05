# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aoi']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['aoi = aoi.base:main']}

setup_kwargs = {
    'name': 'aoi',
    'version': '0.1.2',
    'description': 'SQLITE3 CLI wrapper build on python.',
    'long_description': '# 🍥 aoi\n<p>\n<img src="https://img.shields.io/github/license/sarthhh/aoi?style=flat-square">\n<img src="https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square">\n<img src="https://img.shields.io/github/stars/sarthhh/aoi?style=flat-square">\n<img src="https://img.shields.io/github/last-commit/sarthhh/aoi?style=flat-square">\n<img src="https://img.shields.io/pypi/pyversions/aoi?style=flat-square">\n<img src="https://img.shields.io/pypi/v/aoi?style=flat-square">\n<p>\nA simple python based sqlite3 CLI.\n\n```sh\n$python -m pip install aoi\n```\n---\n\n## Usage \n```sh\n$aoi [-c "path to connect"]\n# if the above fails try executing using full python path. ( read note below image. )\n$python -m aoi [-c "path to connect"]\n```\nusing the -c/--connect option will connect the application to the provided db file path.\n\nIf no option is provided, `:memory:` ( in memory database ) will be used.\n\n## Additional Features\n\nApart from normal sqlite queries you can run the following commands within the CLI:\n\n`:h/:help`: Get help for commands.\n\n`:q/:quit`: Exit the CLI.\n\n`:r/:recent [amount=5]`: Show last [amount=5] queries.\n\n`:t/:tables`: Shows the tables inside the database\n\n\n![](./assets/usage.png)\n\n\n### NOTE\nThe `aoi` command may fail if the executeable\'s path wasn\'t added to the terminal\'s/system\'s PATH, however running the library as a module ( `python -m aoi` ) will always work as long as python is added to path.\n\n---\n## Installation\n* Requires Python (3.8 or later)\n\nInstalling aoi in your environment using pip, poetry or any favourable package manager\n```sh\n# pip\n$pip install aoi # from pypi\n$python -m pip install git+https://github.com/sarthhh/aoi.git # from source\n# poetry\n$poetry add aoi # from pypi\n$poetry add git+https://github.com/sarthhh/aoi.git # from source\n```',
    'author': 'sarthhh',
    'author_email': 'shiva02939@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
