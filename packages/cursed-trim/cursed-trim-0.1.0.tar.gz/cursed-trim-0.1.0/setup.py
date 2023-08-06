# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['cursed_trim']

package_data = \
{'': ['*']}

install_requires = \
['forbiddenfruit>=0.1.2,<0.2.0']

setup_kwargs = {
    'name': 'cursed-trim',
    'version': '0.1.0',
    'description': 'Add a trim attribute to str builtin type',
    'long_description': None,
    'author': 'nqrse',
    'author_email': 'jerome.vlarouche@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
