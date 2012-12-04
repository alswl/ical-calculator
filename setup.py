# -*- coding:utf-8 -*-
"""
Created on Jan 6, 2012

@author: Oberron
"""
from setuptools import setup

setup(
    name = "pyICSParser",
    version = "0.6.1i",
    author = "Oberron",
    author_email = "one.annum@gmail.com",
    description = ("pyICSParser parses icalendar files (.ics or ical files)"
                   " as defined by RFC5545 (previously RFC2445)"
                   "and computes explicit dates for RRULE, EXRULE, RDATE, EXDATE"),
    license = "LICENSE.txt",
    keywords = "ICALENDAR ICAL calendar calendaring event todo journal recurring RFC2445 RFC5545",
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