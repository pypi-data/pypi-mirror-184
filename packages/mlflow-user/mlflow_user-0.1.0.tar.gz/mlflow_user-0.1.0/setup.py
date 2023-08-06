# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlflow_user']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mlflow-user',
    'version': '0.1.0',
    'description': 'A plugin for MLflow to users and permissions',
    'long_description': None,
    'author': 'Abdullah Ahmed',
    'author_email': 'abdullah_ahmed@uk.hrdeu.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
