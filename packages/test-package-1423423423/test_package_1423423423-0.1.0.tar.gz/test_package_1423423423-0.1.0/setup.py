# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test_package_1423423423']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'test-package-1423423423',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'magnus',
    'author_email': 'magnus.maynard@rovco.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
