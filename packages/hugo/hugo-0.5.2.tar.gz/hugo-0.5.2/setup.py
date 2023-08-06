# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['hugo', 'hugo.ext']

package_data = \
{'': ['*']}

install_requires = \
['discord.py']

setup_kwargs = {
    'name': 'hugo',
    'version': '0.5.2',
    'description': 'Discord bot library',
    'long_description': '# Hugo - Discord Bot Library\n\n[![Build Status](https://img.shields.io/travis/Roolat/hugo/develop.svg?style=flat-square)](https://travis-ci.org/Roolat/hugo)\n[![Codecov](https://img.shields.io/codecov/c/github/Roolat/hugo/develop.svg?style=flat-square)](https://codecov.io/gh/Roolat/hugo)\n[![LGTM total alerts](https://img.shields.io/lgtm/alerts/g/Roolat/hugo.svg?style=flat-square)](https://lgtm.com/projects/g/Roolat/hugo/alerts/)\n[![LGTM language grade: Python](https://img.shields.io/lgtm/grade/python/g/Roolat/hugo.svg?style=flat-square)](https://lgtm.com/projects/g/Roolat/hugo/context:python)\n![License](https://img.shields.io/github/license/Roolat/hugo.svg?style=flat-square)\n',
    'author': 'Nariman Safiulin',
    'author_email': 'woofilee@gmail.com',
    'url': 'https://github.com/Roolat/hugo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
