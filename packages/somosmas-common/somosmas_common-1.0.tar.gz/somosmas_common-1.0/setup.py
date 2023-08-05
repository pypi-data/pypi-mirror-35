#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(
    name='somosmas_common',
    version='1.0',
    description=(
        'Package for the software components that are common for the S+ projects',  # noqa
    ),
    author='Omar Diaz',
    author_email='zcool2005@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'requests',
    ],
    zip_safe=False,
)