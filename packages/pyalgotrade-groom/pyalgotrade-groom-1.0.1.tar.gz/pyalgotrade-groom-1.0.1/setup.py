#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: ea-groom
# Mail: earthworm6@163.com
# Created Time:  2018-08-16 11:11:11
# Description: Modfiy for python3
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "pyalgotrade-groom",      #这里是pip项目发布的名称
    version = "1.0.1",  #版本号，数值大的会优先被pip
    keywords = ("pip", "pyalgotrade-groom","pyalgotrade","python3"),
    description = "pyalgotrade for python3",
    long_description = "pyalgotrade Modfiy for python3",
    license = "MIT Licence",

    url = "https://github.com/groom-zhang/pyalgotrade-groom",     #项目相关文件地址，一般是github
    author = "Groom",
    author_email = "earthworm6@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy","pandas","matplotlib"]          #这个项目需要的第三方库
)