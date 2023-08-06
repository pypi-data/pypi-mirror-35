# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    author="Reece Hart",
    author_email="biocommons-dev@googlegroups.com",
    description="alias for the biocommons.seqrepo package",
    name="seqrepo",
    packages=find_packages(),
    url="https://github.com/biocommons/biocommons.seqrepo",
    version='0.0.0',
    zip_safe=True,

    install_requires=[
        "biocommons.seqrepo"
    ]
)
