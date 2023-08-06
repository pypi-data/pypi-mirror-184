#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Jorge Ramiro Alarcon Vargas",
    author_email='jorgeav527@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Trials for the EPIC labs of the Concrete, Soil and Material",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='epic_trials',
    name='epic_trials',
    packages=find_packages(include=['epic_trials', 'epic_trials.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jorgeav527/epic_trials',
    version='0.0.1',
    zip_safe=False,
)
