#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

from MicroTokenizer import __version__, __author__, __email__

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'networkx>=2.1', 'tqdm', 'matplotlib', 'MicroHMM', 'plac']
setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'timer_cm']

setup(
    author=__author__,
    author_email=__email__,
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
    ],
    description="A micro tokenizer for Chinese",
    entry_points={
        'console_scripts': [
            'MicroTokenizer=MicroTokenizer.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='MicroTokenizer',
    name='MicroTokenizer',
    packages=find_packages(include=['MicroTokenizer']),
    data_files=[(
        '',
        [
            'MicroTokenizer/model_data/dict.txt',

            'MicroTokenizer/model_data/A.pickle',
            'MicroTokenizer/model_data/B.pickle',
            'MicroTokenizer/model_data/vocabulary.pickle'
        ]
    )],
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/howl-anderson/MicroTokenizer',
    version=__version__,
    zip_safe=False,
)
