import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openpyxl_utilities",
    version="0.5",
    author="Sebastian Matias Carreira",
    author_email="sebastian.m.carreira@gmail.com",
    description="Library of functions with utilities for the popular xlsx Python module openpyxl",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SebastianMCarreira/openpyxl_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)