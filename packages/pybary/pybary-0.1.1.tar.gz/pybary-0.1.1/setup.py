# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybary']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.12.0,<23.0.0',
 'flake8>=6.0.0,<7.0.0',
 'ipython>=8.8.0,<9.0.0',
 'isort>=5.11.4,<6.0.0',
 'numpy==1.19.5',
 'scipy>=1.10.0,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'pybary',
    'version': '0.1.1',
    'description': 'Barycenter method in python',
    'long_description': '[![Version](https://img.shields.io/pypi/v/pybary.svg)](https://pypi.python.org/pypi/pybary)\n[![python](https://img.shields.io/pypi/pyversions/pybary.svg)](https://pypi.org/project/pybary/)\n\nPybary\n========\n\n![A sniffer optimizer](https://github.com/asmove/pybary/blob/main/images/pybary-tiny.png?raw=true)\n\nBarycenter method in python. Take a look at original article: https://arxiv.org/abs/1801.10533\n\nHow to install\n----------------\n\nWe run the command on desired installation environment:\n\n``` {.bash}\npip install pybary\n```\n\nMinimal example\n----------------\n\nWe may code examples by performing following actions \n\n1. Run command `python examples/example.py` from package root folder;\n2. Open notebook `examples/example.ipynb` and run cell on given order.\n',
    'author': 'Bruno Peixoto',
    'author_email': 'brunolnetto@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/pybary/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<3.12',
}


setup(**setup_kwargs)
