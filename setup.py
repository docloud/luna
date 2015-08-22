#!/usr/bin/env python

from distutils.core import setup
from docloud import __VERSIONS__


entry_points = [
]


setup(name='docloud',
      version=__VERSIONS__,
      description='Docloud Project',
      url='http://github.com/docloud/docloud',
      include_package_data=True,
      entry_points={"console_scripts": entry_points},
      packages=['docloud'],
      #package_data={'folder': ['']},
      #install_requires=open('requirements.txt').readlines(),
     )

