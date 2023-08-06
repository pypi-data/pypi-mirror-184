#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from setuptools import setup, find_packages
import os

MAJOR = 0
MINOR = 1
PATCH = 0
PRE_RELEASE = ''
# Use the following formatting: (major, minor, patch, prerelease)
VERSION = (MAJOR, MINOR, PATCH, PRE_RELEASE)

long_description = "MSAdapter is a toolkit for support the pytorch model runing on ascend.\n"
long_description += "Usage: import ms_adapter.pytorch as ms \n"
long_description += "OpenI: https://openi.pcl.ac.cn/OpenI/MSAdapter \n"
long_description += "Email: pcl.openi@pcl.ac.cn"

def req_file(filename, folder=''):
    with open(os.path.join(folder, filename)) as f:
        content = f.readlines()
    return [x.strip() for x in content]

setup(
    name="ms_adapter",
    version='.'.join(map(str, VERSION[:3])) + ''.join(VERSION[3:]),
    author="Peng Cheng Lab, HUAWEI",
    author_email="pcl.openi@pcl.ac.cn",
    description="MSAdapter is a toolkit for support the pytorch model runing on ascend.",
    long_description=long_description,
    long_description_content_type="text/plain",
    url="https://openi.pcl.ac.cn/OpenI/MSAdapter ",
    packages=find_packages(),
    install_requires=req_file("requirements.txt"),
    classifiers=[
        # How mature is this project? Common values are
        #  1 - Planning 2 - Pre-Alpha 3 - Alpha 4 - Beta 5 - Production/Stable 6 - Mature 7 - Inactive
        'Development Status :: 3 - Alpha',

        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3 :: Only',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: Apache Software License",

        # Indicate what your project relates to
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Additionnal Settings
        'Operating System :: OS Independent',
    ],
    license='Apache 2.0',
    )
