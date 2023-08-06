#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""The setup.py file."""

import os
import sys
from ast import literal_eval

from setuptools import find_packages, setup
from setuptools.command.install import install

# from ramses_rf import __version__ as VERSION


with open("ramses_rf/version.py") as fh:
    for line in fh:
        if line.strip().startswith("__version__"):
            VERSION = literal_eval(line.split("=")[-1].strip())
            break

URL = "https://github.com/zxdavb/ramses_rf"

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

DESCRIPTION = "An interface for the RAMSES RF protocol, "
DESCRIPTION += "as used by Honeywell-compatible HVAC & CH/DHW systems."


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our VERSION."""

    def run(self):
        tag = os.getenv("CIRCLE_TAG")
        if tag != VERSION:
            info = f"The git tag: '{tag}' does not match the package ver: '{VERSION}'"
            sys.exit(info)


setup(
    name="ramses-rf",
    description=DESCRIPTION,
    keywords=["ramses", "evohome", "sundial", "chronotherm", "hometronics"],
    author="David Bonnes",
    author_email="zxdavb@gmail.com",
    url=URL,
    download_url=f"{URL}/archive/{VERSION}.tar.gz",
    install_requires=[val.strip() for val in open("requirements.txt")],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["test", "docs"]),
    version=VERSION,
    license="MIT",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Home Automation",
    ],
    cmdclass={"verify": VerifyVersionCommand},
)
