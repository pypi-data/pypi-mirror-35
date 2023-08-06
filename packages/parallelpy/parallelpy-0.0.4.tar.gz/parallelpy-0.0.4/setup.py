from setuptools import setup, find_packages
import sys, os

version = '0.0.4'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='parallelpy',
      version=version,
      description="A minimal multiprocessing module for data science",
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='multiprocessing data science',
      author='Kyle',
      author_email='todo@todo.com',
      url='https://github.com/krober/parallelpy',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      python_requires='>=3.6',
      )
