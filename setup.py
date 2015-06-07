import os
from setuptools import setup

setup(
    name = "django-jsonfield2",
    version = '15.06.07',
    description = "JSONField for django models",
    long_description = open("README.rst").read(),
    url = "http://bitbucket.org/schinckel/django-jsonfield/",
    author = "Matthew Schinckel",
    author_email = "matt@schinckel.net",
    packages = [
        "jsonfield",
    ],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
    test_suite='tests.main',
    include_package_data=True,
)
