#!  /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import trashtalk


requires = ['pathlib==1.0.1',
            ]

setup(
    name='trashtalk',
    version=trashtalk.__version__,

    packages=find_packages(),

    description="simplify trash in command line",
    long_description=open('README.md').read(),
    url="https://github.com/PTank/trashtalk",
    install_requires=requires,
    include_package_data=True,
    classifier=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Topic :: Utilities"
    ],
    entry_points={
        'console_scripts': [
            'trashtalk = trashtalk.trashtalk:trashtalk',
        ],
    }

)
