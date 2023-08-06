# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['logdecoratorandhandler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'logdecoratorandhandler',
    'version': '0.3.0',
    'description': 'Log decorator and handler for logging functions easily',
    'long_description': None,
    'author': 'barbara73',
    'author_email': 'barbara.jesacher@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
