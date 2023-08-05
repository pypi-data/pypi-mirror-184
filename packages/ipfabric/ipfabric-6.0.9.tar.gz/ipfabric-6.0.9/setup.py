# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ipfabric',
 'ipfabric.settings',
 'ipfabric.technology',
 'ipfabric.tools',
 'ipfabric.tools.factory_defaults',
 'ipfabric.tools.factory_defaults.v4',
 'ipfabric.tools.factory_defaults.v4.4',
 'ipfabric.tools.factory_defaults.v5',
 'ipfabric.tools.factory_defaults.v5.0',
 'ipfabric.tools.factory_defaults.v6',
 'ipfabric.tools.factory_defaults.v6.0']

package_data = \
{'': ['*']}

install_requires = \
['deepdiff>=6.2.2,<7.0.0',
 'httpx>=0.23.2,<0.24.0',
 'ipfabric-httpx-auth>=6.0.0,<7.0.0',
 'macaddress>=2.0.2,<2.1.0',
 'pydantic>=1.8.2,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-dotenv>=0.21,<0.22',
 'pytz>=2022.4,<2023.0']

extras_require = \
{'examples': ['pandas>=1.3.0,<2.0.0',
              'openpyxl>=3.0.9,<4.0.0',
              'tabulate>=0.8.9,<0.10.0',
              'python-json-logger>=2.0.4,<3.0.0',
              'pyyaml>=6.0,<7.0']}

setup_kwargs = {
    'name': 'ipfabric',
    'version': '6.0.9',
    'description': 'Python package for interacting with IP Fabric',
    'long_description': '# IPFabric\n\nIPFabric is a Python module for connecting to and communicating against an IP Fabric instance.\n\n## About\n\nFounded in 2015, [IP Fabric](https://ipfabric.io/) develops network infrastructure visibility and analytics solution to\nhelp enterprise network and security teams with network assurance and automation across multi-domain heterogeneous\nenvironments. From in-depth discovery, through graph visualization, to packet walks and complete network history, IP\nFabric enables to confidently replace manual tasks necessary to handle growing network complexity driven by relentless\ndigital transformation. \n\n## Versioning\nStarting with IP Fabric version 5.0.x the python-ipfabric and python-ipfabric-diagrams will need to\nmatch your IP Fabric version.  The API\'s are changing and instead of `api/v1` they will now be `api/v5.0`.\n\nVersion 5.1 will have backwards compatability with version 5.0 however 6.0 will not support any 5.x versions.\nBy ensuring that your ipfabric SDK\'s match your IP Fabric Major Version will ensure compatibility and will continue to work.\n\n## Installation\n#### Quick Start:\n```\npip install ipfabric\n```\n#### Poetry:\n\nIPFabric uses [Poetry](https://pypi.org/project/poetry/) to make setting up a virtual environment with all dependencies\ninstalled quick and easy.\n\nInstall poetry globally:\n```\npip install poetry\n```\nTo install a virtual environment run the following command in the root of this directory.\n\n```\npoetry install\n```\n\nTo run examples, install extras:\n```\npoetry install ipfabric -E examples\n```\n## Introduction\n\nPlease take a look at [API Programmability - Part 1: The Basics](https://ipfabric.io/blog/api-programmability-part-1/)\nfor instructions on creating an API token.\n\nMost of the methods and features can be located in [Examples](examples) to show how to use this package. \nAnother great introduction to this package can be found at [API Programmability - Part 2: Python](https://ipfabric.io/blog/api-programmability-python/)\n\n## Diagrams\n\nDiagramming in IP Fabric version v4.3 and above has been moved to it\'s own package.\n\n```\npip install ipfabric-diagrams\n```\n\n## Authentication\n### Username/Password\nSupply in client:\n```python\nfrom ipfabric import IPFClient\nipf = IPFClient(\'https://demo3.ipfabric.io/\', username=\'user\', password=\'pass\')\n```\n\n### Token\n```python\nfrom ipfabric import IPFClient\nipf = IPFClient(\'https://demo3.ipfabric.io/\', token=\'token\')\n```\n\n### Environment \nThe easiest way to use this package is with a `.env` file.  You can copy the sample and edit it with your environment variables. \n\n```commandline\ncp sample.env .env\n```\n\nThis contains the following variables which can also be set as environment variables instead of a .env file.\n```\nIPF_URL="https://demo3.ipfabric.io"\nIPF_TOKEN=TOKEN\nIPF_VERIFY=true\n```\n\nOr if using Username/Password:\n```\nIPF_URL="https://demo3.ipfabric.io"\nIPF_USERNAME=USER\nIPF_PASSWORD=PASS\n```\n\n**`IPF_DEV` is an internal variable only, do not set to True.**\n\n## Development\nFollow the poetry install then follow instructions below:\n\nTo test and build:\n\n```\npoetry run pytest\npoetry build\n```\n\nPrior to pushing changes run:\n```\npoetry run black ipfabric\npoetry update\n```\n',
    'author': 'Justin Jeffery',
    'author_email': 'justin.jeffery@ipfabric.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/community-fabric/python-ipfabric',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
