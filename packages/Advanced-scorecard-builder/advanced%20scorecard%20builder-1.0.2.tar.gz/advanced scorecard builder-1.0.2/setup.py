#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Sebastian Zajac'


import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name                = 'advanced scorecard builder',
    version             = '1.0.2',
    description         = ('AMA Institute - Advanced Scorecard Builder Free version'),
    long_description    = read('README.rst'),
    keywords            = ['AMA Institute', 'AMA', 'ASB', 'Scorecard', 'AMA Scorecard'],
    url                 = 'http://amainstitute.pl',
    author              = 's.zajac',
    author_email        = 's.zajac@amainstitute.pl',
    License             = 'MIT',
    classifiers = [

        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities'

    ],
    platforms           = ['Linux','Windows','Mac OS X'],
    packages            = ['AmaFree'],
    install_requires    = ['numpy>=1.11.3', 'pandas>=0.19.2','matplotlib>=2.0.0', 'regressors'],
    project_urls        = {'Source':'https://amainstitute.pl/ama-advanced-scorecard-builder/#start',
                           'Documentation':'https://amainstitute.pl/ama-advanced-scorecard-builder/'}
    )     