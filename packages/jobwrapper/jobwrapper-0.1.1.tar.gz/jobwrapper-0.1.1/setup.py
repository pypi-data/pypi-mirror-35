#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["h5py", "numpy", "matplotlib"]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]


setup(name='jobwrapper',
      version='0.1.1',
      description='Wrappe slurm utilies for python',
      author='Antoine Tavant',
      author_email='antoinetavant@hotmail.fr',
      url="https://github.com/antoinelpp/jobWrapper",
      install_requires=requirements,
      packages=find_packages(include=['jobwrapper']),
      long_description=long_description,
      long_description_content_type="text/markdown",
      test_suite='tests',
      tests_require=test_requirements,
     )
