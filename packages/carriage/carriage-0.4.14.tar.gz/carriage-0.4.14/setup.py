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
['tabulate>=0.8.2,<0.9.0']

extras_require = \
{'all': ['pandas>=0.20,<0.21']}

setup_kwargs = {
    'name': 'carriage',
    'version': '0.4.14',
    'description': 'Enhanced collection classes for programming fluently',
    'long_description': None,
    'author': '顏孜羲',
    'author_email': 'joseph.yen@gmail.com',
    'url': 'http://carriage.readthedocs.io/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
