# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tacitus',
 'tacitus.adapters',
 'tacitus.adapters.sqlalchemy',
 'tacitus.definitions']

package_data = \
{'': ['*']}

install_requires = \
['orjson>=3.8.3,<4.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'sqlalchemy>=1.4.39,<2.0.0']

setup_kwargs = {
    'name': 'tacitus',
    'version': '1.0.2',
    'description': '',
    'long_description': 'None',
    'author': 'Smairon',
    'author_email': 'man@smairon.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
