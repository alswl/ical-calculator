# -*- coding:utf-8 -*-
"""
Created on Jan 6, 2012

@author: Oberron
"""
from setuptools import setup

setup(
    name = "pyICSParser",
    version = "0.6.1h",
    author = "Oberron",
    author_email = "one.annum@gmail.com",
    description = ("pyICSParser parses icalendar files (.ics or ical files)"
                   " as defined by RFC5545 (previously RFC2445)"
                   "and returns json structure with explicit dates "),
    license = "LICENSE.txt",
    keywords = "ICAL parser, ICALENDAR parser, RFC2445 parser, RFC5545 parser)",
    url = "http://ical2list.appspot.com",
    packages=['pyICSParser'],
    package_dir={'pyICSParser': 'src'},
    scripts=['rsc/utest/u_ical.py','rsc/utest/test_vect.py','rsc/utest/u_dateutil_rrul.py'],
    long_description=open('docs/README.txt','rt').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)