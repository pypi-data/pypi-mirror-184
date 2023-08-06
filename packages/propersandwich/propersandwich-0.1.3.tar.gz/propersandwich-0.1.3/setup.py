# -*- coding: utf-8 -*-

# Learn more: https://github.com/senseibara/propersandwich

import pathlib
import importlib
from setuptools import setup, find_packages

readme = pathlib.Path('README.md').read_text()
license = pathlib.Path('LICENSE').read_text()


def collect_dependencies(package_name):
    # Find all the modules in the package
    modules = find_packages(package_name)
    # Import the modules and collect the dependencies
    dependencies = []
    for module in modules:
        imported_module = importlib.import_module(module)
        dependencies.extend(imported_module.__dependencies__)
    return dependencies


setup(
    name='propersandwich',
    version='0.1.3',
    description='propersandwich package',
    long_description=readme,
    author='Senseibara',
    author_email='ndiayebara93@gmail.com',
    url='https://github.com/senseibara/propersandwich',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=collect_dependencies('propersandwich')
)
