#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ConfigFilesManager',
    version='0.1b1',
    description='A python module to a easy manage configs files for applications',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url='https://github.com/orgs/PyModuleManage',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License '
        'v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
    ],
    license='GPL-v3+',
    author='eamanu',
    author_email='eamanu@eamanu.com',
    project_urls={
        'Bug Reports': 'https://github.com/PyModuleManage/ConfigFilesManager/issues',
        'Source': 'https://github.com/PyModuleManage/ConfigFilesManager',
    },
)
