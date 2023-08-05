# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['clouduct', 'clouduct.console', 'clouduct.cookicutter', 'clouduct.reseed']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=2.1,<3.0',
 'boto3>=1.7,<2.0',
 'click-completion',
 'click>=6.7,<7.0',
 'cookiecutter>=1.6,<2.0',
 'npyscreen>=4.10,<5.0',
 'pathspec>=0.5.6,<0.6.0',
 'pyyaml>=3.13,<4.0']

entry_points = \
{'console_scripts': ['clouduct-bootstrap = clouduct.console:main']}

setup_kwargs = {
    'name': 'clouduct',
    'version': '0.0.2',
    'description': 'Bootstrap for Clouduct projects',
    'long_description': None,
    'author': 'Victor Volle',
    'author_email': 'victor.volle@beta-thoughts.org',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
