#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpleloggerplus",
    version="0.0.2",
    author="Stefan Helmert",
    author_email="stefan.helmert@t-online.de",
    description="A simple, easy to use logging tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheTesla/simpleloggerplus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

