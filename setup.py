# -*- coding:utf-8 -*-
"""
Created on Jan 6, 2012

@author: Oberron
"""
from setuptools import setup

setup(
    name = "pyICSParser",
    version = "0.5.2b",
    author = "Oberron",
    author_email = "one.annum@gmail.com",
    description = ("Parses ics files and converts into python array of dates "
                                   "description and uid."),
    license = "LICENSE.txt",
    keywords = "ICS parser",
    url = "http://ical2list.appspot.com",
    packages=['pyICSParser'],
    package_dir={'pyICSParser': 'src'},
    scripts=['bin/ical_test.py','bin/test_vect.py','bin/utest/u_dateutil_rrul.py'],
    long_description=open('docs/README.txt','rt').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)