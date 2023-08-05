# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['finch']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.5.0',
 'distro>=1.7.0',
 'httpx>=0.23.0',
 'pydantic>=1.9.0',
 'typing-extensions>=4.1.1']

setup_kwargs = {
    'name': 'finch-api',
    'version': '0.0.1',
    'description': 'Client library for the Finch API',
    'long_description': '# Finch Python API Library\n\nPlaceholder package for the Finch SDK.\n\n## Documentation\n\nThe API documentation can be found [here](https://developer.tryfinch.com/).\n',
    'author': 'Finch',
    'author_email': 'founders@tryfinch.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Finch-API/finch-api-python',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
