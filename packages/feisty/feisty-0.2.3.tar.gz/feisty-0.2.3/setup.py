# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['feisty']

package_data = \
{'': ['*']}

install_requires = \
['apispec>=0.39.0,<0.40.0', 'falcon>=1.4,<2.0', 'marshmallow>=2.15,<3.0']

entry_points = \
{'console_scripts': ['feisty = feisty.command_line:main']}

setup_kwargs = {
    'name': 'feisty',
    'version': '0.2.3',
    'description': 'Give your Falcon some Swagger',
    'long_description': None,
    'author': 'Adam Gray',
    'author_email': 'acgray@me.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.0.0,<4.0.0',
}


setup(**setup_kwargs)
