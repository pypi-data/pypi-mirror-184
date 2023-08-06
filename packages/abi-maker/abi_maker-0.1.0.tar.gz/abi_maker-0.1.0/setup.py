# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['abi_maker', 'abi_maker.bin', 'abi_maker.template_modules']

package_data = \
{'': ['*'], 'abi_maker': ['demo_abis/*']}

install_requires = \
['inflection>=0.5.1,<0.6.0', 'web3>=5.30.0,<6.0.0']

entry_points = \
{'console_scripts': ['make_abi_wrapper = abi_maker.bin.abi_maker_cli:main']}

setup_kwargs = {
    'name': 'abi-maker',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Athiriyya',
    'author_email': 'athiriyya@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
