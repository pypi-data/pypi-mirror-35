import codecs
import os
import sys


try:
    from setuptools import setup,find_packages
except:
    from distutils.core import setup,find_packages


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
 

NAME = "pyshopee"
PACKAGES = ['hmac','hashlib','requests','urllib']
DESCRIPTION = "Shopee Partners API for python implementation , This is an unofficial Python implementation for the Shopee Partner REST API."
KEYWORDS = "Shopee,Partners API,Shopee Partners API,python-shopee,pyshopee"
AUTHOR = "jimcurrywang & ketu"
AUTHOR_EMAIL = "jimcurrywang@gmail.com"
URL = "https://github.com/JimCurryWang/python-shopee"
VERSION = "1.0.0"
LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    # long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = find_packages(),
    include_package_data=True,
    zip_safe=True,
)
