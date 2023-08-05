# coding=utf-8
"""
Setup file for scale-generator library.
"""

from setuptools import setup

with open("README.md") as readme_fh:
    long_description = readme_fh.read()

setup(
    name="scale-generator",
    version="0.0.2",
    author="Sebastian Dămian",
    author_email="owner@damiancs.ro",
    description="Music scale generator - the only limit is your imagination",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/damiancs/scale-generator/",
    package_dir={"scale-generator": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Intended Audience :: Education",
        "Intended Audience :: Religion",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Artistic Software",
        "Topic :: Education",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Religion",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    license="MIT License",
)
