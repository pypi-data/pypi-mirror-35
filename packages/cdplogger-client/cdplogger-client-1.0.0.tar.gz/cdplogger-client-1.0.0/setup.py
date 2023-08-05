import os
from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()
        
setup(
    name='cdplogger-client',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'promise>=2.1',
        'websocket-client>=0.47.0',
        'protobuf>=3.5.2', 
        'mock>=2.0.0'],
    keywords=["cdp cdpstudio studio client cdp-client cdp_client cdp_logger cdp-logger cdplogger_client cdp_logger_client cdp-logger-client logger"],
    url='', #insert github url
    license='MIT',
    author='CDP Technologies AS',
    author_email='info@cdptech.com',
    description='Provides an API that allows to interact with CDP to access logger data', 
    long_description=readme(),
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6']
)