# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pushcart',
 'pushcart.configuration',
 'pushcart.configuration.presets',
 'pushcart.configuration.validation',
 'pushcart.sources']

package_data = \
{'': ['*']}

install_requires = \
['databricks-cli>=0.17.4,<0.18.0',
 'jobslib>=3.2.0,<4.0.0',
 'param>=1.12.3,<2.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest>=7.2.0,<8.0.0',
 'pyyaml>=6.0,<7.0',
 'tomli>=2.0.1,<3.0.0',
 'traitlets>=5.8.0,<6.0.0']

setup_kwargs = {
    'name': 'pushcart',
    'version': '0.1.4',
    'description': 'Metadata based ingestion and transformation library for Databricks',
    'long_description': '# pushcart\n\nMakes it simpler to move potatoes, bricks or data around.\n',
    'author': 'RevoData B.V.',
    'author_email': 'support@revodata.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
