# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rio_trend', 'rio_trend.scripts']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rio-trend',
    'version': '1.0.0',
    'description': '',
    'long_description': 'None',
    'author': 'zenwalk',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
