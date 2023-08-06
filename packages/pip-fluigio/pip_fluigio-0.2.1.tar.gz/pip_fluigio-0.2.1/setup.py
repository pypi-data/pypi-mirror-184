# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pip_fluigio',
 'pip_fluigio.__fluig_services_base',
 'pip_fluigio.__fluig_services_base.interfaces',
 'pip_fluigio.adapters',
 'pip_fluigio.fluig_services',
 'pip_fluigio.fluig_services.infraestruture',
 'pip_fluigio.tests',
 'pip_fluigio.tests.adapters',
 'pip_fluigio.utils']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'pydantic>=1.10.2,<2.0.0', 'zeep>=4.1.0,<5.0.0']

setup_kwargs = {
    'name': 'pip-fluigio',
    'version': '0.2.1',
    'description': 'abstratct library  services soap plataform fluig',
    'long_description': None,
    'author': 'Rodrigo Becker',
    'author_email': 'rodrigo.beckermore@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
