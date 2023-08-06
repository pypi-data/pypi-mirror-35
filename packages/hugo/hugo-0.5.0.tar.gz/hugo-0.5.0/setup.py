# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['hugo']

package_data = \
{'': ['*']}

install_requires = \
['discord.py>=1.0.0a,<2.0.0']

setup_kwargs = {
    'name': 'hugo',
    'version': '0.5.0',
    'description': 'Discord bot library',
    'long_description': '# Hugo - Discord Bot Library\n',
    'author': 'Nariman Safiulin',
    'author_email': 'woofilee@gmail.com',
    'url': 'https://github.com/narimansafiulin/Hugo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
