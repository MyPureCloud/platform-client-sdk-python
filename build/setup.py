# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "PureCloudPlatformClientV2"
VERSION = "10.0.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name="PureCloudPlatformClientV2",
    version="10.0.0",
    description="PureCloud Platform API SDK",
    author="Genesys Developer Evangelists",
    author_email="DeveloperEvangelists@inin.com",
    url="https://developer.mypurecloud.com/api/rest/client-libraries/python/latest/",
    keywords=["Swagger PureCloud Platform API Genesys"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="A Python library to interface with the PureCloud Platform API"
)


