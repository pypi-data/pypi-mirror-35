#!/usr/bin/python
# -*- coding: UTF-8 -*-


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GadgetBag",
    version="0.0.5",
    author="YanpingDong",
    author_email="lear521@163.com",
    description="A small tool union",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YanpingDong/IndexProject",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
