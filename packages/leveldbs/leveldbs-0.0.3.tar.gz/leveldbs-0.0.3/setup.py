#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: InfinityFuture
# Mail: infinityfuture@foxmail.com
# Created Time: 2018-08-09 02:00:00
#############################################


from setuptools import setup, find_packages

setup(
    name = 'leveldbs',
    version = '0.0.3',
    keywords = ('pip', 'leveldb'),
    description = 'time and path tool',
    long_description = 'time and path tool',
    license = 'MIT Licence',

    url = 'https://github.com/infinityfuture/leveldb-server',
    author = 'infinityfuture',
    author_email = 'infinityfuture@foxmail.com',

    packages = find_packages(),
    include_package_data = True,
    platforms = 'any',
    install_requires = []
)