#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'construct >=2.9, <2.10',
    'Click>=6.0',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Taneli Kaivola",
    author_email='dist@ihme.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Fanuc Remote Buffer interface library",
    entry_points={
#        'console_scripts': [
#            'fanuc_remote_buffer=fanuc_remote_buffer.cli:main',
#        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='fanuc_remote_buffer',
    name='fanuc_remote_buffer',
    packages=find_packages(include=['fanuc_remote_buffer']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://gitlab.com/tanelikaivola/fanuc_remote_buffer',
    version='0.1.3',
    zip_safe=False,
)
