#!/usr/bin/env python
# -*- coding: utf-8 -*-

reqs = map(str.strip, open("requirements.txt").readlines())

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='threes',
    version='0.1.6',
    description='Implementing the tile merge game',
    long_description=readme + '\n\n' + history,
    author='Ben Warren',
    author_email='bwarren2@gmail.com',
    url='https://github.com/bwarren2/threes',
    packages=[
        'threes',
    ],
    package_dir={'threes':
                 'threes'},
    include_package_data=True,
    install_requires=reqs,
    license="BSD",
    zip_safe=False,
    keywords='threes',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=reqs
)
