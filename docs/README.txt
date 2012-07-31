=============
pyICALParser
=============

pyICALParser parses ics (RFC5545 aka ical) files and converts into python array 
[[dates, description, uid]]

Typical usage often looks like this::

	#!/usr/bin/env python
	
	import ical
	
	mycal = ical.ics(start,end)
	#start and end are string objects of yyyymmdd type
	mycal.local_load(file)
	#file being string representation of file location
	mycal.parse_loaded()
	mycal.flatten()
	dates = sorted(mycal.flat_events)
	#dates will contain the array with all explicit events spec'ed by the ics

Paragraphs are separated by blank lines. *Italics*, **bold**,
and ``monospace`` look like this.


Versions
=========

* Pre-alpha
	-v0.0.1: first pre-alpha
	
	-v0.0.27: fixed the dtstart to dtend problem for holiday

* alpha
	-0.4.x: first fully tested handling days - remains to be done is handling of
	time of events
	
Future developments
--------------------
1. handle of datetime (currently only handles date)

2. handle of EXRULE

Thanks
-------
* http://www.tele3.cz/jbar/rest/rest.html: reST to HTML & reST validator
* http://guide.python-distribute.org/creation.html: uploading a package to pypi