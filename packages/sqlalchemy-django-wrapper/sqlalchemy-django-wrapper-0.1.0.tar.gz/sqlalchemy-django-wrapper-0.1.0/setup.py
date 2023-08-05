# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sqlalchemy_wrapper', 'sqlalchemy_wrapper.db', 'tests', 'tests.db']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML==6.0',
 'SQLAlchemy==1.4.41',
 'cfgv==3.3.1',
 'distlib==0.3.6',
 'filelock==3.8.0',
 'greenlet==1.1.3',
 'identify==2.5.5',
 'jsonformatter==0.3.1',
 'nodeenv==1.7.0',
 'platformdirs==2.5.2',
 'psycopg2==2.9.3',
 'pydantic==1.10.2',
 'toml==0.10.2',
 'typing-extensions==4.3.0']

setup_kwargs = {
    'name': 'sqlalchemy-django-wrapper',
    'version': '0.1.0',
    'description': 'A wrapper on top of sqlalchemy that allow to make django orm style query',
    'long_description': '',
    'author': 'Soumaila',
    'author_email': 'admin@cloudmali.ml',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
