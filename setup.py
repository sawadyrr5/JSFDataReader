# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys

sys.path.append('./pyjsf')
sys.path.append('./tests')

setup(
    name='pyjsf',
    version='0.0.1',
    description='Download stock lending data from Japan Security Finance',
    author='@sawadybomb',
    install_requires=['pandas'],
    url='https://twitter.com/sawadybomb/',
    test_suite='test_jsf.suite',
    packages=find_packages(),
)
