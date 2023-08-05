from setuptools import setup, find_packages

setup(packages=find_packages(exclude=('tests', 'docs', 'examples',
                                      'htmlcov', 'build', 'dist')))
