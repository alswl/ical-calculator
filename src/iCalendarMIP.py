# -*- coding:utf-8 -*-
"""iCalendar Message-Based Interoperability Protocol (iMIP) (RFC6048, RFC2447) library

Sends valid email invitations and receives them via SMTP / PoP account

Created on Feb 11, 2013

@author: Oberron
"""

import sys
sys.path.append("../../src/") #to overide previous installs
import icalendar #@UnresolvedImport
import datetime
import smtplib

SMTP_info_file = "C:/sw/misc/SMTP.txt"
""" above file needs to contain 2 lines: first one is the login, 2nd one is the password"""

class iMIP():
    
    """ Generates an email invite (and sends it via SMTP) containing valid iCalendar file
    """
    SMTP_login = ""
    SMTP_password = ""
    def __init__(self):
        SMTP = open(SMTP_info_file).readlines()
        self.SMTP_login = SMTP[0].replace("\n","").replace("\r","")
        self.SMTP_password = SMTP[1].replace("\n","").replace("\r","")
        self.ical = icalendar.ics()

    def CreateiCal(self):
        pass
    def writeMail(self):
        pass
    def sendEmail(self,from_address,to_address,email_as_string):
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(self.SMTP_login, self.SMTP_password)
    #    mailServer.sendmail(fro, attendees, msg.as_string())
        mailServer.sendmail(from_address, to_address, email_as_string)
        mailServer.close()

        
        pass
    
myCal = iMIP()
#print myCal.SMTP_login
#print myCal.SMTP_password

dtstart = datetime.datetime(2013,4,25,9,0,0)
dtend = dtstart + datetime.timedelta(hours =1)
dtstamp= datetime.datetime(2013,2,6,10,11,00)
organizer = "test@test.com"
attendee = "test@test.com"
uid = "CALEVENT_TS090519840000000005"
description = "test"
summary = "test"
location = "Test"
sequence = 1
status = "CONFIRMED"

myCal.ical.events = [{"DTSTART":{"val":dtstart},"DTEND":{"val":dtend},"DTSTAMP":{"val":dtstamp},
                       "ORGANIZER":{"val":organizer,"prop":"CN=Test test"},
                       "ATTENDEE":{"val":attendee},"UID":{"val":uid},
                       "DESCRIPTION":{"val":description},"SUMMARY":{"val":summary},
                       "LOCATION":{"val":location},"SEQUENCE":{"val":sequence},
                       "STATUS":{"val":status}}]

mycal1 =  myCal.ical.Gen_iCalendar(method="REQUEST",append=False)
print "mycal1 is compliant:",myCal.ical.isCalendarStringCompliant(mycal1)
myCal.ical.updateEvent(uid,{"DTSTART":{"val":dtstart+datetime.timedelta(hours=1)},"DTEND":{"val":dtend+datetime.timedelta(hours=1)}})
mycal2 =  myCal.ical.Gen_iCalendar(method="REQUEST",append=False)
print "mycal2 is compliant:",myCal.ical.isCalendarStringCompliant(mycal1)
