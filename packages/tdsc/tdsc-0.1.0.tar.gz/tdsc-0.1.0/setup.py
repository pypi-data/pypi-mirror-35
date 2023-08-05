# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['tdsc', 'tdsc.utils']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4,<2.0', 'distro>=1.3,<2.0', 'six>=1.11,<1.12', 'toml>=0.9,<0.10']

setup_kwargs = {
    'name': 'tdsc',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Liam Dawson',
    'author_email': 'liam@ldaws.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7',
}


setup(**setup_kwargs)
