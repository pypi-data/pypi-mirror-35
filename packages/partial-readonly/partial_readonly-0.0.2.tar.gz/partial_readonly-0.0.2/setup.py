#!/usr/bin/python

from setuptools import setup, find_packages

__author__  = 'book987'
__version__ = '0.0.2'
__license__ = 'MIT'

setup(
    name='partial_readonly',
    version=__version__,
    packages=find_packages(exclude=('tests*',)),
    author=__author__,
    author_email='book78987book@gmail.com',
    description='make some of the dataclass fields read-only',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/book987/partial_readonly',
    license=__license__,
    keywords='dataclass readonly',
    python_requires='>=3.7'
)