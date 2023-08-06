#!/usr/bin/python
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name  = "PyIPAM",
    version = "0.1.4",
    description = "The Simple Python Flask IP Address Manager",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/marknet15/pyipam',
    author='Mark Woolley',
    author_email='mw@marknet15.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        "flask",
        "waitress",
        "psycopg2-binary",
        "ipaddress",
        "configparser"
    ],
    entry_points={
        'console_scripts': [
            'pyipam=pyipam.server:run',
        ],
    }
)