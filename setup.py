import os
from setuptools import setup

setup(
    name = "django-jsonfield2",
    version = '15.06.08',
    license='BSD',
   
    description='A flexible quering JSONField and associated form field to store validated JSON in your model.',
    long_description=open("README.rst").read(),

    install_requires=['Django >= 1.6'],
    tests_require=['Django >= 1.6'],
    
    url = "https://github.com/DarioGT/django-jsonfield2",
    author = "Dario Gomez-Tafur",
    author_email = 'certae.sm@gmail.com',
    
    packages = [
        "jsonfield2",
    ],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='runtest',
    include_package_data=True,
)
