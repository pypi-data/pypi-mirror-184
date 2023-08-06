# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlbands', 'mlbands.neuralnets']

package_data = \
{'': ['*']}

install_requires = \
['mp-api>=0.30.5,<0.31.0',
 'torch>=1.13.1,<2.0.0',
 'torchvision>=0.14.1,<0.15.0']

setup_kwargs = {
    'name': 'mlbands',
    'version': '1.0.0',
    'description': 'A Python package that implements automatic prediction of electronic band gaps for a set of materials based on training data',
    'long_description': '# ML Band Gaps (Materials)\n\n> Ideal candidate: skilled ML data scientist with solid knowledge of materials science.\n\n# Overview\n\nThe aim of this task is to create a python package that implements automatic prediction of electronic band gaps for a set of materials based on training data.\n\n# User story\n\nAs a user of this software I can predict the value of an electronic band gap after passing training data and structural information about the target material.\n\n# Requirements\n\n- suggest the bandgap values for a set of materials designated by their crystallographic and stoichiometric properties\n- the code shall be written in a way that can facilitate easy addition of other characteristics extracted from simulations (forces, pressures, phonon frequencies etc)\n\n# Expectations\n\n- the code shall be able to suggest realistic values for slightly modified geometry sets - eg. trained on Si and Ge it should suggest the value of bandgap for Si49Ge51 to be between those of Si and Ge\n- modular and object-oriented implementation\n- commit early and often - at least once per 24 hours\n\n# Timeline\n\nWe leave exact timing to the candidate. Must fit Within 5 days total.\n\n# Notes\n\n- use a designated github repository for version control\n- suggested source of training data: materialsproject.org\n',
    'author': 'Andrew R. Garcia',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
