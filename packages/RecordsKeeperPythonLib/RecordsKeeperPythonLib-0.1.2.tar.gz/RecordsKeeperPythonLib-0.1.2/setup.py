#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import codecs
from io import open

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    README = f.read()

requires = ["requests", "green", "pyyaml"]

setup(
      name='RecordsKeeperPythonLib',
      version='0.1.2',
      description='RecordsKeeper Python library',
      long_description=README,
      long_description_content_type='text/markdown',
      classifiers=[
          "Programming Language :: Python"
      ],
      url='https://upload.pypi.org/legacy/',
      keywords='recordskeeper, python, library',
      packages=find_packages(),
      zip_safe=False,
      install_requires=requires,
      test_suite="test"
     )
