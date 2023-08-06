#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='bandown',
    version='0.0.1',
    description='A Bandcamp downloader',
    author='Owen Trigueros Sánchez',
    author_email='owentrigueros@gmail.com',
    keywords='bandcamp downloader',
    packages=find_packages(),
    scripts=['bin/bandown'],
    install_requires=[
        'requests',
        'beautifulsoup4'
    ]
)
