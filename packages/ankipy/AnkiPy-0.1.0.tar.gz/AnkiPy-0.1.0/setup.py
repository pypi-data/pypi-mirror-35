# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['ankipy', 'ankipy.tools']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2', 'importlib_resources>=1.0,<2.0']

setup_kwargs = {
    'name': 'ankipy',
    'version': '0.1.0',
    'description': 'Create anki decks and cards from your Python application',
    'long_description': None,
    'author': 'patarapolw',
    'author_email': 'patarapolw@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
