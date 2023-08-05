# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybary']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=8.8.0,<9.0.0', 'numpy==1.19.5', 'scipy>=1.10.0,<2.0.0']

setup_kwargs = {
    'name': 'pybary',
    'version': '0.0.2',
    'description': 'Barycenter method in python',
    'long_description': '[![Version](https://img.shields.io/pypi/v/pybary.svg)](https://pypi.python.org/pypi/pybary)\n[![python](https://img.shields.io/pypi/pyversions/pybary.svg)](https://pypi.org/project/pybary/)\n[![downloads](https://img.shields.io/pypi/dm/pybary)](https://pypi.org/project/pybary/)\n\nPybary\n========\n\n![A sniffer optimizer](https://github.com/asmove/pybary/blob/main/images/pybary-tiny.png?raw=true)\n\nBarycenter method in python. Take a look at original article: https://arxiv.org/abs/1801.10533\n\nHow to install\n----------------\n\nWe run the command on desired installation environment:\n\n``` {.bash}\npip install pybary\n```\n\nMinimal example\n----------------\n\nWe run command `python example.py` on the folder with file `example.py` and following content:\n\n``` {.python}\n#!/usr/bin/env python\nfrom pybary import bary_batch, bary_recursive\nfrom numpy import power, array\nfrom numpy.random import normal\n\n# Oracle function\noracle = lambda x: power(x, 2)\n\n# Initial point\nx0 = array([0, 0])\n\n# Batch points for batch barycenter version\nmu_x = 0\nsigma_x = 1\nsize_x = [100, 2]\n\nxs = normal(mu_x, sigma_x, size_x)\n\n# Hyperparameters\nnu = 10\nsigma = 0.1\nzeta = 0\nlambda_ = 1\niterations = 100\n\n# Recursive run\nxhat_recursive = bary_recursive(\n        oracle, x0, nu, sigma, zeta, lambda_, iterations\n    )\n\n# Batch run\nxhat_batch = bary_batch(\n        oracle, xs, nu, sigma\n    )\n\n# Results\nprint(xhat_batch)\nprint(xhat_recursive)\n```\n',
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
