#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import selecmat

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    name='django-selecmat',

    version=selecmat.__version__,

    packages=find_packages(),

    author="Jorge Batista",

    author_email="jorge.batista@route.technology",

    description="A simple Django form template tag to work with MaterializeCSS and Selectize.js",
    long_description=long_description,
    long_description_content_type="text/markdown",

    include_package_data=True,

    url='https://github.com/dwjorgeb/django-selecmat',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],

    license="MIT",

    zip_safe=False
)
