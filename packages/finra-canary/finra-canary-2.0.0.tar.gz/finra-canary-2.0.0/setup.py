from setuptools import setup, find_packages
import os
import platform
from urllib import request, parse

setup(
    name='finra-canary',
    version='2.0.0',
    license='MIT',
    author="",
    author_email='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='credstashtest project',
    install_requires=[
          'scikit-learn',
          'requests',
      ],
)
