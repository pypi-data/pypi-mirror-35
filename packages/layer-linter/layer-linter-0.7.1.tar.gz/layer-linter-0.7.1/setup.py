#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

try:
    from py_backwards_packager import setup
except ImportError:
    from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'networkx>=2.1,<3',
    'PyYAML>=3.12,<4',
    'click>=6.7,<7',
]

setup_requirements = ['pytest-runner', 'py-backwards-packager']

test_requirements = ['pytest']

setup(
    author="David Seddon",
    author_email='david@seddonym.me',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Layer Linter checks that your project follows a custom-defined layered architecture.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='layer-linter layer-lint',
    name='layer-linter',
    packages=['layer_linter', 'layer_linter.dependencies'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/seddonym/layer_linter',
    version='0.7.1',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'layer-lint = layer_linter.cmdline:main',
        ],
    },
    py_backwards_targets=['3.4', '3.5']
)
