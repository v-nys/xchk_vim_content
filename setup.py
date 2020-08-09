# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xchk_vim_content', 'xchk_vim_content.migrations']

package_data = \
{'': ['*'],
 'xchk_vim_content': ['static/images/*', 'templates/xchk_vim_content/*']}

install_requires = \
[]

setup_kwargs = {
    'name': 'xchk-vim-content',
    'version': '0.0.1',
    'description': 'Course material related to Vim for the xchk teaching framework',
    'long_description': None,
    'author': 'Vincent Nys',
    'author_email': 'vincentnys@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
