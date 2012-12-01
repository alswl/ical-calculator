=============
pyICSParser
=============

pyICSParser parses icalendar files (.ics or ical files) as defined by RFC5545 (previously RFC2445)
and returns json structure with explicit dates [[dates, description, uid]]

Typical usage often looks like this::

	#!/usr/bin/env python
	
	from pyICSParser import ical
	
	mycal = ical.ics(start,end)
	#start and end are string objects of yyyymmdd type
	mycal.local_load(file)
	#file being a string which value is the local path to the icalendar file
	mycal.parse_loaded()
	mycal.flatten()
	dates = sorted(mycal.flat_events)
	#dates will contain the json with all explicit dates of the events spec'ed by the icalendar file

Versions
=========

* Pre-alpha
	-v0.0.1: first pre-alpha
	
	-v0.0.27: fixed the dtstart to dtend problem for holiday

* alpha
	-0.4.x: first fully tested handling days - remains to be done is handling of
	time of events
	
	-0.5.x: added support for EXDATE
	
	-0.6.x: added support for DURATION and when DTEND no present
	
Future developments
--------------------
1. handle of datetime (currently only handles date)
2. handle of EXRULE

Thanks
-------
* http://www.tele3.cz/jbar/rest/rest.html: reST to HTML & reST validator
* http://guide.python-distribute.org/contributing.html: registering a package on pypi and password information
* http://guide.python-distribute.org/creation.html: uploading a package to pypi
* http://blog.msbbc.co.uk/2007/06/using-googles-free-svn-repository-with.html: how to use google codes, subclipse and eclipse