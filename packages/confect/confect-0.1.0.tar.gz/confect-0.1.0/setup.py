# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['confect']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'confect',
    'version': '0.1.0',
    'description': 'Python configuration library that provides pleasant configuration definition and access interface, and it reads unrestricted python configuration file.',
    'long_description': '',
    'author': '顏孜羲',
    'author_email': 'joseph.yen@gmail.com',
    'url': 'https://github.com/d2207197/confect',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
