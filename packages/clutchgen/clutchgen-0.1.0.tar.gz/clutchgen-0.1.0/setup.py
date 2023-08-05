# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clutchGen', 'clutchGen.handlers']

package_data = \
{'': ['*'], 'clutchGen': ['templates/*']}

install_requires = \
['Mako>=1.1.6,<2.0.0', 'PyYAML>=6.0,<7.0', 'click>=8.0.4,<9.0.0']

entry_points = \
{'console_scripts': ['clutchGen = clutchGen.__main__:cli']}

setup_kwargs = {
    'name': 'clutchgen',
    'version': '0.1.0',
    'description': '',
    'long_description': 'This README for develop\ning, read it if you are going to contribute.\n\nInfo about usage you can find on [WIKI pages](https://gitlab.com/AlexeyReket/clutchgen/-/wikis/home)\n\n## Get started\n\nIf you wish you can config your poetry\n\n```shell\npoetry config --local virtualenvs.create true\npoetry config --local virtualenvs.in-project true\n```\n\nInstall required libraries\n\n```shell\npoetry install\n```\n\nActivate created environment\n\n```shell\nsource .venv/bin/activate\n```\n\nand enable autoComplete\n\n```shell\n# for bash\neval "$(_CLUTCHGEN_COMPLETE=bash_source clutchGen)"\n\n# for zsh\neval "$(_CLUTCHGEN_COMPLETE=zsh_source clutchGen)"\n```\n\n## Quality assurance\n\nYou can run tests\n\n```shell\nmake test\n```\n\nAnd can apply formatting:\n\n```shell\nmake format\n```\n\nPlease in case if contributing make tests and save code-style \n',
    'author': 'alexey.reket',
    'author_email': 'alexey.reket@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/AlexeyReket/clutchgen/-/wikis/home',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
