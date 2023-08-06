#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(name='procrun',
      version='1.0.0',
      description='process runner',
      py_modules=['procrun'],
      license='MIT',
      platforms='any',
      install_requires=[])
