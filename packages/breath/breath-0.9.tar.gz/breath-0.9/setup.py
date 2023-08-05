#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import breath

with open('README.md') as readme_file:
	readme = readme_file.read()

requirements = [
	'pyaudio',
	'docopt',
	'pyxhook',
	'peewee',
	'autologging',
	'coloredlogs',
	'inquirer'
]

tests_require = [
]

setup_requires = [
	'setuptools',
	'pip',
	'virtualenv',
	'wheel',
	'twine',
	'bumpversion',
	'setuptools-git'
]

setup(
	name=breath.__name__,
	version=breath.__version__,
	description=breath.__description__,
	long_description=readme,
	long_description_content_type="text/markdown",
	author=breath.__author__,
	author_email=breath.__email__,
	install_requires=requirements,
	setup_requires=setup_requires,
	tests_require=tests_require,
	include_package_data=True,
	packages=find_packages(),
	package_dir={breath.__name__: breath.__name__},
	extras_require={
		'develop': tests_require + setup_requires,
	},
	entry_points={
		'console_scripts': [
			f'{breath.__name__}={breath.__name__}.__main__:cli',
		]
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"Environment :: Console",
		"Operating System :: POSIX :: Linux",
	],

)
