# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ct_util']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.1,<2.0.0', 'pandas>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'ct-util-tools',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'Chris Tran',
    'author_email': 'chris.l.tran.2016@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
