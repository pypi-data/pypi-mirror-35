#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

setup(
    name='somosmas-common',
    version='1.0.5',
    description=(
        'Package for the software components that are common for the S+ projects',  # noqa
    ),
    author='Omar Diaz',
    author_email='zcool2005@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'requests',
      'django-oauth-toolkit'
    ],
    zip_safe=False,
)