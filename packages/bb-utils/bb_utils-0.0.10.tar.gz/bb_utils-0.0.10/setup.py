# coding=utf-8
"""
Setup file for bb_utils module.
"""


from setuptools import find_packages, setup

with open("README.md") as readme_fh:
    long_description = readme_fh.read()

setup(
    name="bb_utils",
    version="0.0.10",
    author="Sebastian Dămian",
    author_email="owner@damiancs.ro",
    description="Bit Breakers Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/bitbreakers/python-libs/bb_utils",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    license="MIT License",
    install_requires=['yoyo-migrations']
)
