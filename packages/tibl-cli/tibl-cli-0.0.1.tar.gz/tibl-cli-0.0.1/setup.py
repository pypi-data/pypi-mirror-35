# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['tibl_cli']

package_data = \
{'': ['*']}

install_requires = \
['blindspin>=2.0,<3.0',
 'click>=6.7,<7.0',
 'crayons>=0.1.2,<0.2.0',
 'gitpython>=2.1,<3.0']

entry_points = \
{'console_scripts': ['tibl = tibl_cli:ui.cli']}

setup_kwargs = {
    'name': 'tibl-cli',
    'version': '0.0.1',
    'description': 'Command Line Interface for tibl, a tiny blog engine.',
    'long_description': None,
    'author': 'uj',
    'author_email': None,
    'url': 'https://ujj.space/tibl-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<3.6',
}


setup(**setup_kwargs)
