#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import dialow as pkg_info

with open("README.md") as fp:
    readme = fp.read()

with open("requirements.txt") as fp:
    requirements = [r.strip() for r in fp.readlines()]


package_name = "pydialogflow"

setup(
    name=package_name,
    packages=find_packages(),
    version=pkg_info.__version__,
    license=pkg_info.__license__,
    author=pkg_info.__author__,
    url="https://github.com/SiLeader/pydialogflow",

    description="Dialogflow API support for Python",
    long_description=readme,
    long_description_content_type="text/markdown",

    install_requires=requirements,

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
