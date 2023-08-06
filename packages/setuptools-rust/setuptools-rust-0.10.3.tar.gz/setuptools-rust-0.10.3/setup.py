#!/usr/bin/env python

from setuptools import setup

version = "0.10.3"

setup(
    name="setuptools-rust",
    version=version,
    author="Nikolay Kim",
    author_email="fafhrd91@gmail.com",
    url="https://github.com/PyO3/setuptools-rust",
    keywords="distutils setuptools rust",
    description="Setuptools rust extension plugin",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["setuptools_rust"],
    install_requires=["semantic_version>=2.6.0", "toml>=0.9.0"],
    zip_safe=True,
    classifiers=[
        "Topic :: Software Development :: Version Control",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points="""
    [distutils.commands]
    check_rust=setuptools_rust.check:check_rust
    clean_rust=setuptools_rust:clean_rust
    build_ext=setuptools_rust:build_ext
    build_rust=setuptools_rust:build_rust
    test_rust=setuptools_rust:test_rust
    tomlgen_rust=setuptools_rust:tomlgen_rust
    """,
)
