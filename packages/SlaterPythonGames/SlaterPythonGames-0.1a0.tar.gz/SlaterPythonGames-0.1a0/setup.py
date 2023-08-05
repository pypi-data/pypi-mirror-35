import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SlaterPythonGames",
    version="0.1a",
    author="Ryan J. Slater",
    author_email="ryan.j.slater.2@gmail.com",
    description="An updated version of rygames, a collection of games written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rjslater2000/SlaterPythonGames",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
