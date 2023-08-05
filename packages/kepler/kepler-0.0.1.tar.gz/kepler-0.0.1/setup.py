#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kepler",
    version="0.0.1",
    author="Jaidev Deshpande",
    author_email="deshpande.jaidev@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaidevd/kepler",
    packages=setuptools.find_packages(),
)
