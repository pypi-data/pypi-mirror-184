#!/usr/bin/env python

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='TaxSEA',
      version='0.0.1',
      description='Taxonomic set enrichment analysis toolkit',
      author='Anders B. Dohlman',
      author_email='abdohlman@gmail.com',
      url='https://github.com/abdohlman/TaxSEA',
      packages=find_packages()
)

