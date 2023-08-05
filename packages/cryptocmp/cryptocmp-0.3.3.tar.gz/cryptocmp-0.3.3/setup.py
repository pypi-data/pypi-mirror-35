#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'requests',
]

setup_requirements = []

test_requirements = []

setup(
    author="Ivan Bogush",
    author_email='bogush.vano@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python3 Wrapper for CryptoCompare public API",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='cryptocmp',
    name='cryptocmp',
    packages=find_packages(),
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    url='https://github.com/OkThought/cryptocmp',
    version='0.3.3',
    zip_safe=False,
)
