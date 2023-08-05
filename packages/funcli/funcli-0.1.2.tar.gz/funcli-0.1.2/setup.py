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

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name = 'funcli',
	version = '0.1.2',
	author = "valtron",
	description = "Automatically generate a simple CLI.",
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	url = 'https://gitlab.com/valtron/funcli',
	py_modules = ['funcli'],
	python_requires = '>=3.6',
	install_requires = [],
	tests_require = tests_require,
	extras_require = { 'test': tests_require },
	cmdclass = { 'test': PyTest },
	classifiers = [
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: MIT License',
	],
)
