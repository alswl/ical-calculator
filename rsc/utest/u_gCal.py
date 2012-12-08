'''
Created on Dec 1, 2012

@author: Oberron
'''

#import gdata 
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
import atom
import getopt
import sys
import string
import time,datetime
from test_vect import testvectors, testvector_path #@UnresolvedImport
import filecmp
import sys
import filecmp
sys.path.append("../../src/") #to overide previous installs
import ical #@UnresolvedImport



class CalendarExample:

    def __init__(self, email, password):
        """Creates a CalendarService and provides ClientLogin auth details to it.
        The email and password are required arguments for ClientLogin.  The
        CalendarService automatically sets the service to be 'cl', as is
        appropriate for calendar.  The 'source' defined below is an arbitrary
        string, but should be used to reference your name or the name of your
        organization, the app name and version, with '-' between each of the three
        values.  The account_type is specified to authenticate either
        Google Accounts or Google Apps accounts.  See gdata.service or
        http://code.google.com/apis/accounts/AuthForInstalledApps.html for more
        info on ClientLogin.  NOTE: ClientLogin should only be used for installed
        applications and not for multi-user web applications."""
    
        self.cal_client = gdata.calendar.client.CalendarClient(source='Google-Calendar_Python_Sample-1.0')
        self.cal_client.ClientLogin(email, password, self.cal_client.source);

    def InsertCalendar(self, title='Little League Schedule',
      description='This calendar contains practice and game times',
      time_zone='America/Los_Angeles', hidden=False, location='Oakland',
      color='#2952A3'):
        """Creates a new calendar using the specified data."""
        print 'Creating new calendar with title "%s"' % title
        calendar = gdata.calendar.data.CalendarEntry()
        calendar.title = atom.data.Title(text=title)
        calendar.summary = atom.data.Summary(text=description)
        calendar.where.append(gdata.calendar.data.CalendarWhere(value=location))
        calendar.color = gdata.calendar.data.ColorProperty(value=color)
        calendar.timezone = gdata.calendar.data.TimeZoneProperty(value=time_zone)
        if hidden:
            calendar.hidden = gdata.calendar.data.HiddenProperty(value='true')
        else:
            calendar.hidden = gdata.calendar.data.HiddenProperty(value='false')
        new_calendar = self.cal_client.InsertCalendar(new_calendar=calendar)
        
        return new_calendar
    
    def InsertRecurringEvent(self,calendar_client, title='Weekly Tennis with Beth',
                             content='Meet for a quick lesson', where='On the courts',
                             recurrence_data=None,dtstart="20081231"):
#        if recurrence_data is None:
#        recurrence_data = ('DTSTART;VALUE=DATE:20081201\r\n'
#        + 'RRULE:FREQ=WEEKLY;BYDAY=Tu;UNTIL=20121231\r\n')
    
        recurrence_data = "DTSTART;VALUE=DATE:"+dtstart+"\r\n"+recurrence_data
#        recurrence_data = "DTSTART;VALUE=DATE:20081229\r\nRRULE:FREQ=WEEKLY;INTERVAL=1"
        print "recurence rule:",recurrence_data
        event = gdata.calendar.data.CalendarEventEntry()
        event.title = atom.data.Title(text=title)
        event.content = atom.data.Content(text=content)
#        event.uid = "1annumt"
        event.where.append(gdata.calendar.data.CalendarWhere(value=where))
    
        # Set a recurring event
        event.recurrence = gdata.data.Recurrence(text=recurrence_data)
        new_event = calendar_client.InsertEvent(event)

#        print 'New recurring event inserted: %s' % (new_event.id.text,)
#        print '\tEvent edit URL: %s' % (new_event.GetEditLink().href,)
#        print '\tEvent HTML URL: %s' % (new_event.GetHtmlLink().href,)
    
        return new_event
    
    def DateRangeQuery(self,calendar_client, title,uid,start_date, end_date):
#        print 'Date range query for events on Primary Calendar: %s to %s' % (start_date, end_date,)
#        print "date window:",start_date,end_date
        query = gdata.calendar.client.CalendarEventQuery()
        query.start_min = '2011-01-01'
        query.start_max = '2013-01-01'
        feed = calendar_client.GetCalendarEventFeed(q=query)
#        print "feed",feed
        res = open(tmp,'w')
        for i, an_event in enumerate(feed.entry):
#            print "line 99",an_event.title.text
            if an_event.title.text == title:
#                print '\t%s. %s' % (i, an_event.title.text,)
                line = ""
                for a_when in an_event.when:
                    dtstart = datetime.datetime.strptime(a_when.start,"%Y-%m-%d").strftime("%Y%m%d")
                    line = '{datetime-start: %s, summary: %s, uid: %s}\n' % (dtstart,an_event.title.text,uid)
#                    print line
#                    print 'Event %s,\t\tStart time: %s,\t\tEndtime: %s' % (an_event.title.text,a_when.start,a_when.end,)
#                    print '\t\tEnd time:   %s' % ()
                    res.write(line)
                    line = ""
        res.close()

user = 'test.ical2list@gmail.com'
pw = 'xLRqvP3anTKW6jE8rW7X'

def Run_Test_Vectors():
    sample = CalendarExample(user, pw)
    EventDescription = "utest gcal"

    print "entering test vectors"
    for vect in testvectors[15:20]:
        [locfile,start,end,reference] = vect
        mycal = ical.ics(start,end)
        mycal.debug(False,"../../out/log.txt")
        mycal.local_load(testvector_path+locfile)
        mycal.parse_loaded()
        [sdtstart,dtend,rules, summary,suid,rdates,exdates] = mycal.events[0]
#        summary = "IC04 weekly"
        ddtstart=str(sdtstart.strftime("%Y%m%d"))
        
#        print rules

        rrule = "RRULE:"
        for prop in rules:
#            print prop, rules[prop]
            rrule+=prop+"="+str(rules[prop])+";"

        rrule = rrule[:-1]
#        print rrule
                
        ree = sample.InsertRecurringEvent(sample.cal_client,title=summary,recurrence_data=rrule,dtstart=ddtstart)
        startdate=datetime.datetime.strptime(start,"%Y%m%d").strftime("%Y-%m-%d")
        enddate=datetime.datetime.strptime(end,"%Y%m%d").strftime("%Y-%m-%d")
        sample.DateRangeQuery(sample.cal_client,title=summary,uid=suid,start_date=startdate, end_date=enddate)

        if filecmp.cmp(tmp,testvector_path+reference,shallow = False):
            print vect,"\t - OK"
        else:
            print vect,"\t - NOK"
            sys.exit()

        sample.cal_client.Delete(ree)

tmp = "c:/sw/ical2pdf/out/tmp.txt"
Run_Test_Vectors()

#sample.Run(delete)
