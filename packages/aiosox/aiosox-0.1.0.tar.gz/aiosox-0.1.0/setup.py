# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiosox',
 'aiosox.asyncapi',
 'aiosox.kafka',
 'aiosox.ponicode',
 'aiosox.sio',
 'aiosox.sio.ponicode']

package_data = \
{'': ['*']}

install_requires = \
['aiokafka>=0.8.0,<0.9.0',
 'anyio[trio]>=3.6.2,<4.0.0',
 'fastapi>=0.88.0,<0.89.0',
 'mkdocs-material>=9.0.2,<10.0.0',
 'mkdocs>=1.4.2,<2.0.0',
 'orjson>=3.8.3,<4.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'python-socketio>=5.7.2,<6.0.0',
 'uvicorn[standard]>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'aiosox',
    'version': '0.1.0',
    'description': '⛓️ Combination of asyncapi(documentation) & socketio pub/sub using aiokafka as the client manager  multinode backend services',
    'long_description': '\nhypercorn main:app --worker-class trio --reload\n\npoetry config repositories.aiosox https://pypi.example.org/legacy/\n',
    'author': 'Arie',
    'author_email': 'ariesorkin3@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/arieutils/aiosox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.11.1',
}


setup(**setup_kwargs)
