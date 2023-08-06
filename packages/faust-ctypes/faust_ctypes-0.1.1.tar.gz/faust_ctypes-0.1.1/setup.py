# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faust_ctypes']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.18.0']

setup_kwargs = {
    'name': 'faust-ctypes',
    'version': '0.1.1',
    'description': "a port of Marc Joliet's FaustPy to Ctypes",
    'long_description': "# Faust Ctypes\n\n## include Faust compiled DSP into Python\n\na port of Marc Joliet's [FaustPy](https://github.com/marcecj/faust_python) from\n[CFFI](https://cffi.readthedocs.org/) to\n[Ctypes](https://docs.python.org/3/library/ctypes.html)\n\n## Introduction\n\n[FAUST](https://faust.grame.fr/) is a programming language dedicated to sound\nsynthesis and audio processing. Faust-Ctypes provides a way to compile a faust\ncode into a dynamically linked library(DLL), which can then be called from any\nPython program as a simple Python library thanks to the CTypes library.\n\n## Documentation\n\nFaust-Ctypes documentation is available online at https://adud2.gitlab.io/faust-ctypes/\n",
    'author': 'Antonin Dudermel',
    'author_email': 'antonin.dudermel@caramail.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
