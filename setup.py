#!/usr/bin/env python

from setuptools import setup, find_packages

entry_points = [
    'doclient=docloud.commands.cli:cli'
]


setup(
    name='docloud',
    version='0.0.1',
    description='Docloud Project Client',
    url='http://github.com/docloud/docloud',
    include_package_data=True,
    packages=find_packages(),
    entry_points={"console_scripts": entry_points},
    #package_data={'folder': ['']},
    install_requires=open('requirements.txt').readlines(),
)

