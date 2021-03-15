# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in library1_management/__init__.py
from library1_management import __version__ as version

setup(
	name='library1_management',
	version=version,
	description='Library Management System',
	author='Harry Code',
	author_email='harry@example.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
