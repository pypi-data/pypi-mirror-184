# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['akira']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.2,<2.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest>=7.2.0,<8.0.0',
 'pyyaml>=6.0,<7.0']

setup_kwargs = {
    'name': 'akira',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Bruno-Felix',
    'author_email': 'balvesfelix@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
