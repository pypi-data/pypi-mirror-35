# -*- coding: utf-8 -*-
from setuptools import setup

import papis_rofi

with open('README.rst') as fd:
    long_description = fd.read()

setup(
    name='papis-rofi',
    version=papis_rofi.__version__,
    author='Alejandro Gallo',
    author_email='aamsgallo@gmail.com',
    license='GPLv3',
    url='https://github.com/papis/scripts/tree/master/papis-rofi',
    install_requires=[
        "papis>=0.7",
        "papis-python-rofi>=1.0.1",
        "click",
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    description='Rofi based inerface for papis',
    long_description=long_description,
    keywords=[
        'papis', 'rofi', 'bibtex',
        'management', 'cli', 'biliography'
    ],
    packages=[
        "papis_rofi",
    ],
    entry_points=dict(
        console_scripts=[
            'papis-rofi=papis_rofi.main:main'
        ]
    ),
    platforms=['linux', 'osx'],
)
