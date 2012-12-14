'''
Created on Nov 27, 2012

@author: a0919149
'''
import unittest
import sys,datetime
sys.path.append("../../src/") #to overide previous installs
import ical #@UnresolvedImport
from test_vect import testvectors, testvector_path #@UnresolvedImport


class Test(unittest.TestCase):


    def setUp(self):
        self.testDuration()
        self.testRRULEgen()
        pass


    def tearDown(self):
        pass

    def testRRULEgen(self):
        print "testing RRULE gen"
        mycal = ical.ics()
        mycal.debug(True,LogPath="../../out/log.txt",debug_level=0)
        cal = testvectors[10]
        [locfile,start,end,reference] = ["12OL.ics","20110101","20121231","12OL.txt"]

        mycal.local_load(testvector_path + locfile)
        mycal.parse_loaded()
        RRULE = mycal.GenRRULEstr(mycal.events[0][2])
        assert RRULE == "RRULE:FREQ=YEARLY;INTERVAL=1;BYMONTH=4;BYMONTHDAY=1;WKST=SU"
        
    def testDuration(self):
        print "testing Duration parsing"
        mycal = ical.ics("20120101","20120101")
        """RFC2445 p37
        Example: A duration of 15 days, 5 hours and 20 seconds would be:
        P15DT5H0M20S
        """
        res = mycal.ParseDuration("P15DT5H0M20S")
        assert res == datetime.timedelta(days = 15, hours = 5, seconds = 20)
        
        """
        A duration of 7 weeks would be:
        P7W
        """
        res = mycal.ParseDuration("P7W")
        assert res == datetime.timedelta(weeks = 7) 
        
        """
        The period start at 18:00:00 on January 1, 1997 and lasting 5 hours
        and 30 minutes would be:        
        19970101T180000Z/PT5H30M
        """
        res = mycal.ParseDuration("PT5H30M")
        assert res == datetime.timedelta(hours = 5, minutes=30) 
        
        """
        rfc2445 p71
        15 minute 
        PT15M
        """
        res = mycal.ParseDuration("PT15M")
        assert res == datetime.timedelta(minutes=15) 
        
        """
        rfc2445 p71
        30 minutes before the scheduled start of the event
        -PT30M
        """
        res = mycal.ParseDuration("-PT30M")
#        print "res 61:",res
#        print datetime.timedelta(minutes = -30)
        assert res == datetime.timedelta(minutes=-30) 
        
        """
        rfc2445 p72
        one hour intervals
        PT1H
        """
        res = mycal.ParseDuration("PT1H")
        assert res == datetime.timedelta(hours = 1) 
        
        """
        RFC2445 p94
        interval of time of 1 hour and zero minutes and zero seconds
        PT1H0M0S
        """
        res = mycal.ParseDuration("PT1H0M0S")
        assert res == datetime.timedelta(hours = 1,minutes = 0, seconds =0) 
        
        """
        rfc2445 p126
        with a 5 minute delay
        PT5M
        """
        res = mycal.ParseDuration("PT5M")
        assert res == datetime.timedelta(minutes = 5) 
        
        print "end test on duration parsing"
#        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
#    tt = Test()
#    tt.testDuration()
#    tt.testRRULEgen()
    [locfile,start,end,reference] = ["12OL.ics","20110101","20121231","12OL.txt"]
    locfile = "./test_vect/" +locfile
    mycal = ical.ics(start,end)
    mycal.debug(True,LogPath="../../out/log.txt",debug_level=0)
    mycal.local_load(locfile)
    mycal.parse_loaded()
    RRULE = mycal.GenRRULEstr(mycal.events[0][2])
    assert RRULE == "RRULE:FREQ=YEARLY;INTERVAL=1;BYMONTH=4;BYMONTHDAY=1;WKST=SU"
    [locfile,start,end,reference] = ["15OL.ics","20110101","20121231","12OL.txt"]
    locfile = "./test_vect/" +locfile
    mycal = ical.ics(start,end)
    mycal.debug(True,LogPath="../../out/log.txt",debug_level=0)
    mycal.local_load(locfile)
    mycal.parse_loaded()
    RRULE = mycal.GenRRULEstr(mycal.events[0][2])
    print RRULE
    assert RRULE == "RRULE:FREQ=YEARLY;INTERVAL=1;BYMONTH=4;BYDAY=SA,SU;BYSETPOS=1;WKST=SU"
