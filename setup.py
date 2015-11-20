#!/usr/bin/env python

from setuptools import setup, find_packages

entry_points = [
    'luna=luna.commands.cli:cli'
]

setup(
    name='luna',
    version='0.0.1',
    description='Luna Project',
    url='http://github.com/luna/luna',
    include_package_data=True,
    packages=find_packages(),
    entry_points={"console_scripts": entry_points},
    # package_data={'folder': ['']},
    install_requires=open('requirements.txt').readlines(),
)
