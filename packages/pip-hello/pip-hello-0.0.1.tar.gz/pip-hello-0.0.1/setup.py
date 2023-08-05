#!/usr/bin/env python

#############################################
# File Name: setup.py
# Author: yeyuel
# Mail: dx1988226@gmail.com
# Created Time:  2018-8-21 19:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name="pip-hello",
    version="0.0.1",
    keywords=("pip", "hello", "hello world"),
    description="pip install test",
    long_description="time and path tool",

    url="https://github.com/yeyuel/pip-hello.git",
    author="yeyuel",
    author_email="dx1988226@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)