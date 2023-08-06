# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thumbnails_readme']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.4.0,<10.0.0', 'pdf2image>=1.16.2,<2.0.0']

setup_kwargs = {
    'name': 'thumbnails-readme',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Rok Kukovec',
    'author_email': 'rok.kukovec1@um.si',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
