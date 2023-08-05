# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['dir2md']
install_requires = \
['fire>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['dir2md = dir2md:main']}

setup_kwargs = {
    'name': 'dir2md',
    'version': '0.1.0',
    'description': '',
    'long_description': '# dir2md\n\n`dir2md` is a command line utility for creating a markdown file that includes code blocks for all specified files.\n\n## Installation\n\nInstall dir2md using pip:\n\n```bash\npip install dir2md\n```\n\n## Usage\n\nTo use `dir2md`, pass a list of file paths as arguments:\n\n```bash\ndir2md file1.py file2.py\n```\n\nThis will output a markdown file with code blocks for `file1.py` and `file2.py`.\n\n### Wildcard support\n\nYou can use wildcards (`*`) to pass multiple files at once.\n\nFor example, to include all Python files in the current directory:\n\n```bash\ndir2md *.py\n```\n\nTo do so recursively, use `**`:\n\n```bash\ndir2md **/*.py\n```\n\nNote that the wildcard statement only works if it is expanded by the shell before the command is run. This means that you must use it in the command line or in a shell script, and it will not work if you pass it as a string to a function that runs the command.\n\n\n## Options\n\nUse the `--help` flag to view the available options:\n\n```bash\ndir2md --help\n```\n',
    'author': 'IsaacBreen',
    'author_email': 'mail@isaacbreen.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
