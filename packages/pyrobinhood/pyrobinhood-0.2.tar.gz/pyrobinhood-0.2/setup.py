try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools import find_packages

setup(name='pyrobinhood',
      version='0.2',
      description='Python Robinhood client',
      author='Daniel Wang',
      author_email='danielwpz@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      install_requires=[
          'requests'
      ],
      zip_safe=False)
