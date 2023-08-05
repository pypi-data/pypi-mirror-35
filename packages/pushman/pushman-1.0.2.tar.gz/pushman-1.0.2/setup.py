# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.2'


setup(
    name='pushman',
    version=version,
    keywords='',
    description='Python binding for Pushman',
    long_description=open('README.rst').read(),

    url='https://github.com/Pushmen/Pushman-Python',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['pushman'],
    py_modules=[],
    install_requires=[],

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
