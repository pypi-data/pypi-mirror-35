from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="data_lib",
    version="1.0.0",
    author="Adam Jarzebak",
    author_email="adam@jarzebak.eu",
    description="Data handling and manipulation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jarzab3/data_lib.git",
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ),
)
