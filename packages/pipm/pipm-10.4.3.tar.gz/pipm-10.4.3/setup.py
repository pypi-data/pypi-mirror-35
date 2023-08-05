# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pipm']

package_data = \
{'': ['*']}

install_requires = \
['pip>=10', 'six>=1.11,<2.0']

entry_points = \
{'console_scripts': ['pipm = pipm:main']}

setup_kwargs = {
    'name': 'pipm',
    'version': '10.4.3',
    'description': 'Wrapper around pip commands to auto-update requirements file',
    'long_description': "# pipm\n\nPython package management workflow using pip, requirements file & setup.cfg as its metadata. \n(For the time being and old world of python)\n\n# Installation\n\n- Adviced to install only inside virtualenv as this will replace pip executable\n\nInstall from PyPI\n\n```\npip install six\npip install pipm\n```\n\nOr Install directly from the GitHub\n\n```commandline\npip install -e git://github.com/jnoortheen/pipm.git@master#egg=pipm\n```\n\n**Note:**\n- This tool manipulates all your requirements file. So be sure to use version control software or take backup of your files to keep track of changes. \n\n# Quickstart\nBoth `pip` and `pipm` command will work as the same. Create an alias as `alias pip=pipm` and you are good to go.   \n\n### install all your dependencies from the requirements file\n\n- to install only from `requirements.txt` \n\n```pipm install```\n\n- to install from all `*requirements*.txt`\n\n```pipm install --all```\n\n### installation\n```pipm install pkg-name``` or \n```pip install pkg-name```\n\n### installation as development dependency\n```pipm install pkg-name --dev```\n\n\n### installation as testing dependency\n```pipm install pkg-name --test```\n\n### removal \n```pipm uninstall pkg-name```\n\n### update all your dependencies\n```pipm update```\n\n### including development dependencies\n```pipm install --dev```\n\n\n# Usage\n\n1. install\n    - a wrapper around standard `pip install` command and accepts all the standard options\n    \n    Below are the things that `pipm` brings to the table\n    \n    1. Extra functionality\n        - when package names are given it will be saved to the requirements.txt file in the current directory.\n        If you have `requirements` directory structure with `base.txt` inside then that file will be used. Otherwise it \n        will create one in the current directory.\n        - when no package name is given then it is equivalent to `-r requirements.txt` and it will install all requirements\n        from the current directory\n    1. Additional options:\n        the below saves to file when package name given otherwise equivalent to passing requirements file name.\n        1. `--dev` - saves to development requirements\n        1. `--prod` - saves to production requirements\n        1. `--test` - saves to  testing requirements\n        1. `--env <name>` - if you have any special set of requirements that belong to a separate file you could pass the name here.\n        It will search for the matching one in the following pattern `<name>-requirements.txt` or \n        `requirements/<name>.txt` or `requirements-<name>.txt`\n\n1. uninstall \n    - a wrapper around standard `pip uninstall` command\n    - alias `rm` is available\n    - when uninstalling a package, this command also checks packages that are no longer required by any of the installed\n    packages and removes them\n    - ofcourse it removes the packages from `requirements` files\n\n1. update\n    - new command\n    - equivalent to calling `pip install` with `--upgrade` flag\n    - update a single package or the whole environment when no argument given.\n    - by default the packages are updated interactively\n        - set `--auto-update` to disable this\n\n1. save/freeze\n    - extends the standard freeze command to save the currently installed packages\n\n\n# Features\n\n1. Just a wrapper around the standard pip's `install/uninstall` command. So all the cli options will work\n2. Handles multiple `requirements` files\n3. No new set of files. requirements files contain pinned dependecies and setup.cfg contain abstract dependencies.\n\n# Development\n- clone the repository and create new virtualenv\n\n```\ngit clone git@github.com:jnoortheen/pipm.git\ncd pipm\npew new pipm -a .\npip install -r dev-requirements.txt\n```\n\n-  to test from local sources\n```\npip install -e .\n```\n\n# Testing\n\n- run `invoke test` from the root directory.\n\n# Version compatibility\n\nthe package is versioned in accordance with `pip` major version number. \n`pipm-9.*` will be compatible with `pip-9` and such.\n\n# Alternatives and their problems (IMHO)\n\n1. [pipenv](https://docs.pipenv.org/) \n    - good for local development with only one virtual environment per project\n    - Not good when we need to deploy over production server or keep multiple virtuals-envs\n    - it is better to use `pew` alone instead of the shell command that comes with this\n2. [pip-tools](https://github.com/jazzband/pip-tools)\n    - another set of files to keep track of, additional commands to remember\n3. [poetry](https://github.com/sdispater/poetry) \n    - better than pipenv and do not interfere much in environment management with pew\n    - the problems I faced are related to installing dependencies in remote servers/docker environments. \n    As the project matures this problem might get resolved. \n",
    'author': 'jnoortheen',
    'author_email': 'jnoortheen@gmail.com',
    'url': 'https://github.com/jnoortheen/pipm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*',
}


setup(**setup_kwargs)
