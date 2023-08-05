#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008 Noah Kantrowitz
# Copyright (C) 2012-2017 Ryan J Ollos
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.


import os

from setuptools import setup

setup(
    name='TracPrivateTickets',
    version='2.3.0',
    packages=['privatetickets'],

    author='Noah Kantrowitz',
    author_email='noah@coderanger.net',
    maintainer='Ryan J Ollos',
    maintainer_email='ryan.j.ollos@gmail.com',
    description='Modified ticket security for Trac.',
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README')).read(),
    license='BSD 3-Clause',
    keywords='trac plugin ticket permissions security',
    url='https://trac-hacks.org/wiki/PrivateTicketsPlugin',
    classifiers=[
        'Framework :: Trac',
    ],

    entry_points={
        'trac.plugins': [
            'privatetickets.policy = privatetickets.policy',
        ],
    },
    install_requires=['Trac'],
    test_suite='privatetickets.tests.test_suite',
)
