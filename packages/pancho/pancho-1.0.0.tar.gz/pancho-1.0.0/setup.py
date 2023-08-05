# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pancho',
 'pancho.bootstraping',
 'pancho.context',
 'pancho.definitions',
 'pancho.definitions.contracts',
 'pancho.definitions.exceptions',
 'pancho.exploration',
 'pancho.identity',
 'pancho.interaction',
 'pancho.markup',
 'pancho.obtaining',
 'pancho.operations',
 'pancho.processing',
 'pancho.state']

package_data = \
{'': ['*']}

install_requires = \
['orjson>=3.8.3,<4.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'tacitus>=1.0.0,<2.0.0',
 'zorge>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'pancho',
    'version': '1.0.0',
    'description': 'Commands and queries processor',
    'long_description': 'None',
    'author': 'sergey feofilaktov',
    'author_email': 'feofilaktov@rpharm.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
