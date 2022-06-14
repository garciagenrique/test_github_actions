#!/usr/bin/env python

import setuptools

# Define entry points for command-line scripts

setuptools.setup(name='test_actions',
                 version='v0.1',
                 description="Test github actions",
                 install_requires=['numpy'],
                 tests_require=['pytest'],
                 author='https://github.com/garciagenrique',
                 author_email='garcia<at>lapp.in2p3.fr',
                 )  
