import sys
import setuptools
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
	user_options = [
		('pytest-args=', 'a', "Arguments to pass to pytest")
	]
	
	def initialize_options(self):
		super().initialize_options()
		self.pytest_args = ''
	
	def run_tests(self):
		import shlex
		import pytest
		args = self.pytest_args
		# Undo MSYS path translation
		args = args.replace(';', '::')
		args = args.replace('\\', '/')
		sys.exit(pytest.main(shlex.split(args)))

tests_require = ['pytest']

setuptools.setup(
	name = 'funcli',
	version = '0.1.0',
	author = "valtron",
	description = "Turn commandline args into function calls",
	url = 'https://gitlab.com/valtron/funcli',
	packages = setuptools.find_packages(exclude = ['tests*']),
	python_requires = '>=3.5',
	install_requires = [],
	tests_require = tests_require,
	extras_require = { 'test': tests_require },
	cmdclass = { 'test': PyTest },
	classifiers = [
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: MIT License',
	],
)
