#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('pandoc --from=markdown --to=rst -o README.rst README.md')
    os.system('python setup.py sdist upload')
    sys.exit()

README = open('README.md').read()
HISTORY = open('CHANGES.txt').read().replace('.. :changelog:', '')

setup(
    name='sjcl',
    version='0.2.1',
    description="Decrypt and encrypt messages compatible to the 'Stanford Javascript Crypto Library (SJCL)' message format.",
    long_description=README + '\n\n' + HISTORY,
    author='Ulf Bartel',
    author_email='elastic.code@gmail.com',
    url='https://github.com/berlincode/sjcl',
    packages=[
        'sjcl',
    ],
    package_dir={'sjcl': 'sjcl'},
    include_package_data=True,
    install_requires=['pycryptodome'],
    license="new-style BSD",
    zip_safe=False,
    keywords='SJCL, AES, encryption, pycrypto, Javascript',
    entry_points={
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
)
