# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apache_arrow_practice']

package_data = \
{'': ['*']}

install_requires = \
['pyarrow>=10.0.1,<11.0.0']

setup_kwargs = {
    'name': 'apache-arrow-practice',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'dev-owner',
    'author_email': 'yureka1112@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
