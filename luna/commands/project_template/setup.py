#!/usr/bin/env python
# coding=utf8

"""
Copyright 2015 {{project}}
"""

from setuptools import setup, find_packages

setup(
    name='{{project}}',
    version='0.0.1',
    description='{{project}} Project',
    include_package_data=True,
    packages=find_packages(),
    install_requires=open('requirements.txt').readlines(),
)
