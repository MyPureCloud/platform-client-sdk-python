# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "PureCloudPlatformClientV2"
VERSION = "229.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.26.20", "certifi >= 2025.01.31", "python-dateutil >= 2.9.0.post0", "watchdog >= 5.0.0"]

setup(
    name="PureCloudPlatformClientV2",
    version="229.0.0",
    description="PureCloud Platform API SDK",
    author="Genesys Developer Evangelists",
    author_email="DeveloperEvangelists@Genesys.com",
    url="https://mypurecloud.github.io/platform-client-sdk-python/",
    keywords=["Swagger PureCloud Platform API Genesys"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="A Python library to interface with the PureCloud Platform API",
    long_description_content_type="text/plain",
    license="MIT",
    python_requires=">=3.9"
)
