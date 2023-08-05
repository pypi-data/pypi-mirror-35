# -*- coding: utf-8 -*-
from __future__ import print_function

from os import chdir
from os.path import abspath, dirname

from setuptools import find_packages, setup

chdir(dirname(abspath(__file__)))

with open('README.rst') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    author='Brandon Davidson',
    author_email='brad@oatmail.org',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP',
    ],
    description='Uses AuthN/AuthZ environment variables from Apache mod_authnz_ldap to enforce access controls on Flask apps',
    extras_require={
        'dev': [
            'setuptools-version-command',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    long_description=readme,
    name='flask-authnz-ldap-rbac',
    packages=find_packages(exclude=('docs')),
    python_requires='>=2.7',
    url='https://github.com/brandond/flask-authnz-ldap-rbac',
    version_command=('git describe --tags --dirty', 'pep440-git-full'),
)
