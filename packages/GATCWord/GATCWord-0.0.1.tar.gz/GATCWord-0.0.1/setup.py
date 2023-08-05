# -*- coding: utf-8 -*-
# !/usr/bin/python
# Create Date 2018/8/23 0023
__author__ = 'huohuo'
from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name = 'GATCWord',
    version = '0.0.1',
    keywords = ('word', 'test'),
    description = 'generate word',
    license = 'MIT License',

    author = 'hp910219',
    author_email = 'hp910219@126.com',
    url='https://github.com/hp910219/jy_word.git',

    packages = find_packages(exclude=['test']),
)
if __name__ == "__main__":
    pass
    

