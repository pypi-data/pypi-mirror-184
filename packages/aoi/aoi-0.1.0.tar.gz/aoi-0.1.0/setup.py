# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aoi']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.6,<0.5.0']

setup_kwargs = {
    'name': 'aoi',
    'version': '0.1.0',
    'description': 'SQLITE3 CLI wrapper build on python.',
    'long_description': '# 🍥 aoi\nA simple python based sqlite3 CLI.\n\n---\n\n## Usage \n```sh\n$python -m aoi [-c "path to connect"]\n```\nusing the -c/--connect option will connect the application to the provided db file path.\n\nIf no option is provided, `:memory:` ( in memory database ) will be used.\n\n## Additional Features\n\nApart from normal sqlite quries you can run the following commands within the CLI:\n\n`:h/:help`: Get help for commands.\n\n`:q/:quit`: Exit the CLI.\n\n`:r/:recent [amount=5]`: Show last [amount=5] queries.\n\n---\n## Requirements\n* Python (3.8 or later)\n\nInstalling aoi in your environment using pip, poetry or any favourable package manager\n```sh\n# pip\n$python -m pip install git+https://github.com/sarthhh/aoi.git\n# poetry\n$poetry add git+https://github.com/sarthhh/aoi.git\n```',
    'author': 'sarthhh',
    'author_email': 'shiva02939@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
