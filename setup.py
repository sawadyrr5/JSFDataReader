# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys

sys.path.append('./pyjsf')
sys.path.append('./tests')

setup(
    name='pyjsf',
    version='0.0.2',
    description='Download loans for margin transaction data from web',
    author='@sawadybomb',
    install_requires=['pandas==0.18.1'],
    url='https://twitter.com/sawadybomb/',
    test_suite='test_jsf.suite',
    packages=find_packages(),
)
