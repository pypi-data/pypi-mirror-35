# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['od_client']

package_data = \
{'': ['*']}

install_requires = \
['requests']

setup_kwargs = {
    'name': 'od-client',
    'version': '0.1.0',
    'description': 'Python client for Oxford Dictionaries API',
    'long_description': 'Oxford dictionaries http client\n===============================\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/ambv/black\n    :alt: code style: black\n\nInstall\n-------\n\n::\n\n    pip install od-client\n\n\nNote\n----\n\nThis package is under development.\n\nDocumentation\n-------------\n\nFull documentation is available at https://od-client.readthedocs.io/en/latest/.\n\nLicense\n-------\n\nMIT licensed. See the `LICENSE <https://github.com/apologist/oxford-dictionaries-client/blob/master/LICENSE>`_ file for more details.',
    'author': 'Oleksii',
    'author_email': '_@apologist.io',
    'url': 'https://github.com/apologist/oxford-dictionaries-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
