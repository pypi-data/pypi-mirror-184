# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boltlib']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1,<9.0',
 'loguru>=0.6,<0.7',
 'ndeflib>=0.3,<0.4',
 'pyscard>=2.0,<3.0']

entry_points = \
{'console_scripts': ['boltcard = boltlib.cli:cli']}

setup_kwargs = {
    'name': 'boltlib',
    'version': '0.1.0',
    'description': 'Bitcoin Lightning BoltCard (NTAG 424 DNA) Read/Write library',
    'long_description': '# boltlib - Bitcoin Lightning BoltCard library\n\n[![Tests](https://github.com/titusz/boltlib/actions/workflows/tests.yml/badge.svg)](https://github.com/titusz/boltlib/actions/workflows/tests.yml)\n\n`boltlib` is a Python library and command line tool for easy reading and writing of\n[BoltCards](https://boltcard.org) based on [pyscard](https://github.com/LudovicRousseau/pyscard)\n\n## Requirements\n\n- [Python 3.8](https://www.python.org/) or higher.\n- Smart Card Reader (USB CCID class-compliant)\n\nTested with `Identiv uTrust 3700F` but should work with others like for example `ACS ACR1252U` or\n`HID Omnikey 5022 CL`.\n\n> **Note**: On Ubuntu/Debian run `sudo apt-get install libpcsclite-dev swig` before installation.\n\n## Installation\n\n```shell\n$ pip install boltlib\n```\n\n## Command line usage\n\n```shell\n$ boltcard\nUsage: boltcard [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --version     Show the version and exit.\n  -s, --silent  Silence debug output.\n  --help        Show this message and exit.\n\nCommands:\n  read   Read BoltCard UID and URI\n  write  Write URI to BoltCard (unprovisioned only)\n```\n\n## Library usage\n\n```python\nimport boltlib\nuri = boltlib.read_uri()\nprint(uri)\n```\n\n## Development\n\n### Requirements\n- [Python 3.8](https://www.python.org/) or higher.\n- [Poetry](https://python-poetry.org/) for installation and dependency management.\n\n### Setup\n\n```shell\ngit clone https://github.com/titusz/boltlib.git\ncd boltlib\npoetry install\n```\n\n### Run Tasks\n\nBefore committing changes run code formatting and tests with:\n\n```shell\npoe all\n```\n\n\n',
    'author': 'Titusz',
    'author_email': 'tp@py7.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/titusz/boltlib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
