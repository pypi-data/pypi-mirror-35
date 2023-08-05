# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['carriage']

package_data = \
{'': ['*'],
 'carriage': ['.mypy_cache/*',
              '.mypy_cache/3.6/*',
              '.mypy_cache/3.6/collections/*',
              '.ropeproject/*']}

install_requires = \
['pandas[all]>=0.23.3,<0.24.0', 'tabulate>=0.8.2,<0.9.0']

setup_kwargs = {
    'name': 'carriage',
    'version': '0.4.13',
    'description': 'Enhanced collection classes for programming fluently',
    'long_description': None,
    'author': '顏孜羲',
    'author_email': 'joseph.yen@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
