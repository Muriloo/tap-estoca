#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-estoca",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Muriloo",
    url="https://github.com/Muriloo",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_estoca"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-estoca=tap_estoca:main
    """,
    packages=["tap_estoca"],
    package_data = {
        "schemas": ["tap_estoca/schemas/*.json"]
    },
    include_package_data=True,
)
