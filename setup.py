#!  /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import trashtalk

print(find_packages())
setup(
    name='trashtalk',
    version=trashtalk.__version__,

    packages=find_packages(),

    description="simplify trash in command line",

    url="https://github.com/PTank/trashtalk",

    classifier=[
        "Programming Language :: Python",
    ],
    entry_points={
        'console_scripts': [
            'trashtalk = trashtalk.trashtalk:trashtalk',
        ],
    }

)
