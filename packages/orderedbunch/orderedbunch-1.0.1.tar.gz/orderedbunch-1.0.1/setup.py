#from distutils.core import setup
from setuptools import setup, find_packages

# import __version__
exec(open('orderedbunch/_version.py').read())

setup(
    name='orderedbunch',
    version=__version__,
    author='Nathan Longbotham',
    author_email='longbotham@gmail.com',
    packages=find_packages(),
    description='Tab completable ordered dictionary.',
    long_description=open('README.rst').read(),
    test_suite = 'orderedbunch.test'
)
