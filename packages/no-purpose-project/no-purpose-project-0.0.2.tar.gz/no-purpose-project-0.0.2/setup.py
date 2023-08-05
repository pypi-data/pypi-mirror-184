from os import path

from setuptools import setup

BASE_DIR = path.abspath(path.dirname(__file__))


setup(
    name='no-purpose-project',
    version='0.0.2',
    description='Library for creating nothing',
    long_description='Library for creating nothing',

    author='Over Lucker',
    author_email='lucker1005000@gmail.com',
    url='https://github.com/OverLucker/no-purpose-project',

    license='WTF PL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ],
    keywords='',
)