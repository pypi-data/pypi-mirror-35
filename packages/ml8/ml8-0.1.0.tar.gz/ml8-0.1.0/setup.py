#!/usr/bin/env python

import re


try:
    from setuptools import setup,find_packages
except ImportError:
    from distutils.core import setup


version = '0.1.0'

if not version:
    raise RuntimeError('Cannot find version information')


with open('README.rst', 'rb') as f:
    readme = f.read().decode('utf-8')

setup(
    name='ml8',
	author='Jiao Shuai',
	author_email='jiaoshuaihit@gmail.com',
    version=version,
    description='TechYoung Machine Learning ToolKit',
    long_description=readme,
    packages=find_packages(exclude=["doc","examples","test"]),
    install_requires=['requests!=2.9.0','crcmod>=1.7'],
    include_package_data=True,
    url='http://ml8.techyoung.cn',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
)
