#!/usr/bin/env python3

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

NAME = "cophi"
DESCRIPTION = "A library for preprocessing."
URL = "https://github.com/cophi-wue/cophi-toolbox"
AUTHOR = "Chair of Computer Philology and Modern German Literary History"
EMAIL = None
REQUIRES_PYTHON = ">=3.4.0"
VERSION = None

REQUIRED = [
    "pandas>=0.23.4",
    "numpy>=1.15.0",
    "lxml>=4.2.4",
    "regex>=2018.07.11"
]

here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    with open(os.path.join(here, "src", NAME, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages("src"),
    package_dir={'': 'src'},
    install_requires=REQUIRED,
    include_package_data=True,
    license="Apache 2.0",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ]
)
