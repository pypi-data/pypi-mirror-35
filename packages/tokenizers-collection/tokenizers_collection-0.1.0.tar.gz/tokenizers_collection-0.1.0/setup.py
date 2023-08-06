#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'requests', 'jieba', 'thulac', 'pynlpir', 'pyltp']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Xiaoquan Kong",
    author_email='u1mail2me@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A simple iterator for using a set of Chinese tokenizer",
    entry_points={
        'console_scripts': [
            'tokenizers_collection=tokenizers_collection.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tokenizers_collection',
    name='tokenizers_collection',
    packages=find_packages(include=['tokenizers_collection']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/howl-anderson/tokenizers_collection',
    version='0.1.0',
    zip_safe=False,
)
