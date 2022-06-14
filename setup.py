#!/usr/bin/env python

import setuptools
import test_github_actions

# Define entry points for command-line scripts
entry_points = {'console_scripts': ['square_number = test_github_actions.test:main']}


setuptools.setup(name='test_actions',
                 version='v0.1',
                 description="Test github actions",
                 install_requires=['numpy'],
                 tests_require=['pytest'],
                 author='https://github.com/garciagenrique',
                 author_email='garcia<at>lapp.in2p3.fr',
                 entry_points=entry_points,
                 )  
