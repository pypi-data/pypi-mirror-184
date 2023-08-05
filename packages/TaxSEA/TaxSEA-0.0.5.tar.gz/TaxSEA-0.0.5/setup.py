# -*- coding: utf-8 -*-
 
 
"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup
 
 
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('TaxSEA/TaxSEA.py').read(),
    re.M
    ).group(1)
 
 
with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='TaxSEA',
    packages=['TaxSEA'],
    entry_points = {
        "console_scripts": ['TaxSEA = TaxSEA.TaxSEA:main']
    },
    version = version,
    description='Taxonomic set enrichment analysis toolkit',
#    long_description = long_description,
#    long_description_content_type='text/markdown',
    author='Anders B. Dohlman',
    author_email='abdohlman@gmail.com',
    url='https://github.com/abdohlman/TaxSEA',
)
