# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ls_tree']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['ls-tree = ls_tree.cli:run']}

setup_kwargs = {
    'name': 'ls-tree-py',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Andrei Fokau',
    'author_email': 'andrei@fokau.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://...',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
