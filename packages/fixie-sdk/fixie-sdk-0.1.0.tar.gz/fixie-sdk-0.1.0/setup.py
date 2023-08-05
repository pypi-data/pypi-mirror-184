# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fixie']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'gql[all]>=3.4.0,<4.0.0',
 'pillow>=9.0.1,<10.0.0',
 'requests>=2.28.1,<3.0.0',
 'rich>=12.6.0,<13.0.0']

setup_kwargs = {
    'name': 'fixie-sdk',
    'version': '0.1.0',
    'description': 'SDK for the Fixie platform. See: https://fixie.ai',
    'long_description': 'None',
    'author': 'Fixie.ai Team',
    'author_email': 'founders@fixie.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
