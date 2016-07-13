#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 07:14:20 2015

@author: ddboline
"""
from __future__ import (absolute_import, division, print_function)

from setuptools import setup

setup(
    name='entrypoints',
    version='0.2.2',
    author='Thomas Kluyver',
    author_email='thomas@kluyver.me.uk',
    description='entrypoints',
    long_description='entrypoints',
    license='MIT',
    install_requires=['configparser'],
    py_modules = ['entrypoints']
)
