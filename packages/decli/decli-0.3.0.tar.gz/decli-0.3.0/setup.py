# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['decli']

package_data = \
{'': ['*'],
 'decli': ['.pytest_cache/*', '.pytest_cache/v/*', '.pytest_cache/v/cache/*']}

setup_kwargs = {
    'name': 'decli',
    'version': '0.3.0',
    'description': 'Minimal, easy-to-use, declarative cli tool',
    'long_description': None,
    'author': 'Santiago Fraire',
    'author_email': 'santiwilly@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>3.6',
}


setup(**setup_kwargs)
