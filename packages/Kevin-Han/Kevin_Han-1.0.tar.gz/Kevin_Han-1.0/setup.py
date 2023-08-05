#!/user/bin/python3 
# -*- coding: utf-8 -*-
'''
@Time:2023-01-05 10:20:33
@Author:Kevin_Han
@File:setup.py
@Email:1737770324@qq.com
@QQ:1737770324
'''
from distutils.core import  setup
import setuptools
packages = ['Kevin_Han']# 唯一的包名，自己取名
setup(name='Kevin_Han',
	version='1.0',
	author='Kevin_Han',
    packages=packages,
    package_dir={'requests': 'requests'},)
