# from distutils.core import setup
from setuptools import setup, find_packages

import t2

# import unittest


# def my_test_suite():
#     test_loader = unittest.TestLoader()
#     test_suite = test_loader.discover('tests', pattern='test_*.py')
#     return test_suite

setup(name=t2.__name__,
      version=t2.__version__,
      description='Module for backdoor design and implementation.',
      url=t2.__github__,
      author=t2.__author__,
      author_email=t2.__email__,
      license='MIT',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
	  keywords = ['crypto', 'covert', 'backdoor', 'shell']
    #   zip_safe=False,
	#   tests_require=['entropy',
	#   'pytest==2.9.2'
	#   ],
	#   test_suite = 'setup.my_test_suite'
	  )