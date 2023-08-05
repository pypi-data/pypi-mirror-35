import setuptools
import os
import sys

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='SlaterPythonGames',
    version="0.22a",
    description="An updated version of rygames, a collection of games written in Python",
    author="Ryan J. Slater",
    author_email="ryan.j.slater.2@gmail.com",
    url="https://github.com/rjslater2000/SlaterPythonGames",
    packages=setuptools.find_packages(),
    include_package_data=True,
    long_description_content_type='text/x-rst',
    long_description=read('README.rst'),
    keywords=['games', 'battleship', 'python'],
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"],
    install_requires=['pygame', 'numpy', 'matplotlib', 'names'],
    )
