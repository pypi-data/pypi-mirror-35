# -*- coding: utf-8 -*-
# !/usr/bin/python
# Create Date 2018/6/4 0004
__author__ = 'huohuo'
from setuptools import setup, find_packages

setup(
    name = 'jy-word',
    version = '0.5',
    keywords = ('word', 'test'),
    description = 'generate word',
    license = 'MIT License',

    author = 'hp910219',
    author_email = 'hp910219@126.com',
    url='https://github.com/hp910219/jy-word.git',

    packages = find_packages(exclude=['test']),
)

if __name__ == "__main__":
      pass
    

