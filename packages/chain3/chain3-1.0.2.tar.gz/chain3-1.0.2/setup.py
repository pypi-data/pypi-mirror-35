﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)

setup(
    name='chain3',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='1.0.2',
    description="""Chain3.py for moac""",
    #long_description_markdown_filename='README.md',
    author='Michael Wang',
    author_email='wangxi@moacchina.com',
	url='https://github.com/moac/chain3.py',
    include_package_data=True,
    install_requires=[
        "cytoolz>=0.9.0,<1.0.0;implementation_name=='cpython'",
    ],
    setup_requires=['setuptools-markdown'],
    python_requires='>=3.5, <4',
    license="MIT",
    zip_safe=False,
    keywords='moac',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
