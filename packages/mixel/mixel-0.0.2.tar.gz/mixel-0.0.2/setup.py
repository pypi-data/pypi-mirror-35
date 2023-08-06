from setuptools import setup,find_packages
from setuptools.extension import Extension
import numpy

setup(
  name='mixel',
  version='0.0.2',
  author='Lawrence Pang',
  author_email='lawrencepang36@gmail.com',
  description='a small python module for recoloring images with pixels from a palette image',
  url='https://github.com/lpang36/mixel',
  packages=find_packages(),
  ext_modules=[Extension('anneal',['anneal.c'])],
  include_dirs=[numpy.get_include()],
  py_modules=['main'],
  platforms=['any'],
  license='MIT',
  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 2",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
  ]
)