# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['montecarlosim']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.0,<3.7.0', 'numpy>=1.24.0,<1.25.0']

entry_points = \
{'console_scripts': ['tests = run_tests:run']}

setup_kwargs = {
    'name': 'montecarlosim',
    'version': '0.1.0',
    'description': 'MonteCarlo simulation library',
    'long_description': "# MonteCarlo simulation algorithm\n\n## Installation\n`pip install montecarlosim`\n\n## Requirements\nPython 3.10.0+\nCurrently working to introduce support to old version.\n\n## Getting started\n- Clone the repository the way you like;\n- Create a virtualenv (with pyenv and virtualenv you can run `pyenv virtualenv 3.10.0 <name_you_like>`) otherwise install poetry and run `poetry install`, it will take care of the virtualenv itself;\n- Now you can lunch the tests with `poetry run tests` and it will tests all environment inside tox.ini `envlist`;\n- Create a branch, do your changes, push them and open a PR.\n\n## Repository structure\nRepository configuration files are:\n- `pyproject.toml`;\n- `tox.ini`, tests;\n- `src`, contains the actual repository code;\n- `src/montecarlo.py`, contains the Montecarlo class (where magic happens);\n- `src/functions.py`, contains example functions to be used with Montecarlo class;\n- `src/exceptions.py`, contains custom exception that are used to better handle errors;\n- `tests`, contains python tests file that is launched by tox;\n- `run_tests.py`, simple function that run `subprocess.run('tox')`.",
    'author': 'Valerio Farrotti',
    'author_email': 'valerio.farrotti@gmail.com',
    'maintainer': 'Valerio Farrotti',
    'maintainer_email': 'valerio.farrotti@gmail.com',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10.0,<4.0.0',
}


setup(**setup_kwargs)
