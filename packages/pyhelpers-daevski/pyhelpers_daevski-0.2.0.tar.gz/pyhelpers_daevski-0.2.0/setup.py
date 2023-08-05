# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyhelpers_daevski']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=39.0.0,<40.0.0', 'pyyaml>=6.0,<7.0']

setup_kwargs = {
    'name': 'pyhelpers-daevski',
    'version': '0.2.0',
    'description': 'helper functions for personal use',
    'long_description': '# pyhelpers\n\nPersonal python package for helper functions.\n',
    'author': 'David Mckee',
    'author_email': 'daevski@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
