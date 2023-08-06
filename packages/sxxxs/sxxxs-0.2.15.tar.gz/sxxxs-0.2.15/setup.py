# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sxxxs', 'sxxxs..sc']

package_data = \
{'': ['*'],
 'sxxxs': ['.idea/*', '.idea/inspectionProfiles/*'],
 'sxxxs..sc': ['web/*', 'web/assets/*']}

entry_points = \
{'console_scripts': ['aaa = sxxxs.main:main']}

setup_kwargs = {
    'name': 'sxxxs',
    'version': '0.2.15',
    'description': '',
    'long_description': '',
    'author': 'sss',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
