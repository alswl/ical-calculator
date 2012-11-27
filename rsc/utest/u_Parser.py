'''
Created on Nov 27, 2012

@author: a0919149
'''
import unittest
import sys,datetime
sys.path.append("../../src/") #to overide previous installs
import ical #@UnresolvedImport


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testDuration(self):
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
        
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()