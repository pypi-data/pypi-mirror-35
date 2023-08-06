#!/usr/bin/env python

from setuptools import setup, find_packages
import versioneer

install_requires = [
    'boto3>=1.7.45',
    'pandas>=0.23.1',
    'botocore>=1.10.45',
    'pyyaml>=3.12',
    'cx_Oracle>=6.0b2',
    'sqlalchemy >= 1.2.8',
    'pyarrow >= 0.9.0',
    'fastparquet >= 0.1.5'
]

setup(
    name='eqi-utils',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Common utilities for EQI project.',
    long_description=open('README.rst').read(),
    author='Jinpeng Zhang',
    author_email='jinzha098718@gmail.com',
    url='https://github.com/jinzha098718/eqi-utilities',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(include='eqi_utils.*'),
    install_requires=install_requires
)
