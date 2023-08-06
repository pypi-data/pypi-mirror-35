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
    'version': '0.0.2',
    'description': 'Command Line Interface for tibl, a tiny blog engine.',
    'long_description': '# 🗿 tibl-cli\n\n[tibl](https://github.com/Uinelj/tibl) python command line interface.\n\n\n## Features \n\n```\nUsage: tibl [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  create  Create a new tibl site\n  items   list posts and pages\n  new     Create a new post/page\n  serve   serve your website locally\n```\n\n## Installing\n\ntibl-cli is  available in PyPI.\n\n```bash\npip install tibl-cli\n```\n',
    'author': 'uj',
    'author_email': None,
    'url': 'https://ujj.space/tibl/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
