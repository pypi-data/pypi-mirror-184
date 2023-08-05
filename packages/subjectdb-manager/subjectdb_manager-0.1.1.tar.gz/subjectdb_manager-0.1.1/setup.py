# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['subjectdb_manager']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['subjectdb_manager = '
                     'subjectdb_manager.subjectdb_manager:cli']}

setup_kwargs = {
    'name': 'subjectdb-manager',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'Greg Schwimer',
    'author_email': 'schwim@bitrail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
