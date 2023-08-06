#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from setuptools import setup

with open("seutils/include/VERSION", "r") as f:
    version = f.read().strip()

setup(
    name          = 'seutils',
    version       = version,
    license       = 'BSD 3-Clause License',
    description   = 'Description text',
    url           = 'https://github.com/tklijnsma/seutils.git',
    author        = 'Thomas Klijnsma',
    author_email  = 'tklijnsm@gmail.com',
    packages      = ['seutils'],
    package_data  = {'seutils': ['include/*']},
    include_package_data = True,
    zip_safe      = False,
    scripts       = [
        'bin/seu-install-completion',
        'bin/seu-version',
        # SE interactions
        'bin/seu-ls', 'bin/seu-du',
        'bin/seu-rm', 'bin/seu-mkdir', 'bin/seu-cat',
        # ROOT-file interactions
        'bin/seu-root-ls', 'bin/seu-root-count',
        # 'bin/seu-nentries', 'bin/seu-printbranches',
        # 'bin/seu-countdataset'
        ]
    )
