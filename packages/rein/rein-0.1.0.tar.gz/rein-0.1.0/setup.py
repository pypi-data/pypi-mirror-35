#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'click>=6.7',
    'python-dateutil>=2.7.3',
    'autobahn>=18.6.1',
    'Twisted>=18.7.0',
    'blinker>=1.4',
    'pyOpenSSL>=18.0.0',
    'bidict>=0.17.2',
    'namedlist>=1.7',
    'aiohttp>=2.3.10',
    'requests>=2.19.1',
    'SQLAlchemy>=1.2.10',
    'mysql-connector>=2.1.6',
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    author="Chris Chen",
    author_email='chrischen3121@gmail.com',
    name='rein',
    keywords='rein',
    version='0.1.0',
    description="lightweight trading platform",
    long_description=readme + '\n\n' + history,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    url='https://github.com/chrischen3121/rein',
    license="Apache Software License 2.0",
    packages=find_packages(include=['rein'], exclude=['docs', 'tests']),
    package_data={},
    data_files=[
        # (os.path.expanduser("~/.rein/docs"), ["docs/index.rst"]),
        # (os.path.expanduser("~/.rein/config"), ["rein/config.py"]),
    ],
    python_requires='>=3.5.3',
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    test_suite='tests',
    # scripts=['bin/rein'],
    # entry_points={
    #     'console_scripts': [
    #         'rein=rein.cli:main',
    #     ],
    # },
    include_package_data=True,
    zip_safe=False,
)
