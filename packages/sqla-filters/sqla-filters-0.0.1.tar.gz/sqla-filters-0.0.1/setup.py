# -*- coding: utf-8 -*-
"""sqla-filters setup file."""
import os
from typing import List
from setuptools import (
    setup,
    find_packages,
)


VERSION: str = '0.0.1'
DESCRIPTION: str = 'Library to help developer to create filter for the sqlachemy orm.'

REQUIRE: List[str] = [
    'sqlalchemy'
]

DEV_REQUIRE: List[str] = [
    'pylint',
    'pep8',
    'autopep8',
    'ipython',
    'mypy',
    'pytest',
    'rope'
]

def read(file_path: str):
    with open(file_path) as f:
        return f.read()

setup(
    name='sqla-filters',
    version=VERSION,
    description=DESCRIPTION,
    long_description=read(os.path.join(os.path.dirname(__file__), 'README.md')),
    long_description_content_type='text/markdown',
    url='https://github.com/MarcAureleCoste/sqla-filters',

    author='Marc-Aurele Coste',

    license='MIT',
    zip_safe=False,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    install_requires=REQUIRE,
    packages=find_packages('src'),
    package_dir={'': 'src'},

    entry_points={},

    tests_require=DEV_REQUIRE,
    extras_require={
        'dev': DEV_REQUIRE
    }
)
