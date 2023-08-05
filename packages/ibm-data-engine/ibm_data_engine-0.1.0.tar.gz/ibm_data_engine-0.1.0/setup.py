# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ibm_data_engine']

package_data = \
{'': ['*']}

install_requires = \
['feast>=0.25.0,<0.26.0', 'ibmcloudsql>=0.5.11,<0.6.0']

setup_kwargs = {
    'name': 'ibm-data-engine',
    'version': '0.1.0',
    'description': 'Feast offline feature store implementation backed by the IBM Cloud Data Engine',
    'long_description': 'None',
    'author': 'Michal Siedlaczek',
    'author_email': 'michal.siedlaczek@ibm.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
