# -*- coding: utf-8 -*-
# !/usr/bin/python
# Create Date 2018/6/4 0004
__author__ = 'huohuo'
from setuptools import setup, find_packages
import ConfigParser
import os
cfg_path = os.path.join(os.path.dirname(__file__), 'config.cfg')
cfg = ConfigParser.ConfigParser()
cfg.read(cfg_path)
version = cfg.get('pastescript', 'version')

setup(
    name='jy-word',
    version=version.strip(),
    keywords=('word', 'test'),
    description='generate word',
    license='MIT License',
    author='hp910219',
    author_email='hp910219@126.com',
    url='https://github.com/hp910219/jy-word.git',
    packages=find_packages(exclude=['test']),
)

if __name__ == "__main__":
    pass