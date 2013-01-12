'''
Created on Nov 27, 2012

@author: Oberron
'''
import unittest
import filecmp
import sys,datetime
sys.path.append("../../src/") #to overide previous installs
import icalendar #@UnresolvedImport
from test_vect import rrule_vects, testvector_path #@UnresolvedImport


class TestIcalParser(unittest.TestCase):

    def setUp(self):
        self.mycal = icalendar.ics()
        self.vevent = icalendar.vevent()

        pass

    def tearDown(self):
        pass
        
    def test_Duration(self):
#        print "testing Duration parsing"
        mycal = icalendar.ics()
        """RFC2445 p37
        Example: A duration of 15 days, 5 hours and 20 seconds would be:
        P15DT5H0M20S
        """
        res = self.vevent.duration_load("P15DT5H0M20S")
#        print "line 33",res, "---",datetime.timedelta(days = 15, hours = 5, seconds = 20)
        assert res == datetime.timedelta(days = 15, hours = 5, seconds = 20)
        
        """
        A duration of 7 weeks would be:
        P7W
        """
        res = self.vevent.duration_load("P7W")
        assert res == datetime.timedelta(weeks = 7) 
        
        """
        The period start at 18:00:00 on January 1, 1997 and lasting 5 hours
        and 30 minutes would be:        
        19970101T180000Z/PT5H30M
        """
        res = self.vevent.duration_load("PT5H30M")
        assert res == datetime.timedelta(hours = 5, minutes=30) 
        
        """
        rfc2445 p71
        15 minute 
        PT15M
        """
        res = self.vevent.duration_load("PT15M")
        assert res == datetime.timedelta(minutes=15) 
        
        """
        rfc2445 p71
        30 minutes before the scheduled start of the event
        -PT30M
        """
        res = self.vevent.duration_load("-PT30M")
#        print "res 61:",res
#        print datetime.timedelta(minutes = -30)
        assert res == datetime.timedelta(minutes=-30) 
        
        """
        rfc2445 p72
        one hour intervals
        PT1H
        """
        res = self.vevent.duration_load("PT1H")
        assert res == datetime.timedelta(hours = 1) 
        
        """
        RFC2445 p94
        interval of time of 1 hour and zero minutes and zero seconds
        PT1H0M0S
        """
        res = self.vevent.duration_load("PT1H0M0S")
        assert res == datetime.timedelta(hours = 1,minutes = 0, seconds =0) 
        
        """
        rfc2445 p126
        with a 5 minute delay
        PT5M
        """
        res = self.vevent.duration_load("PT5M")
        assert res == datetime.timedelta(minutes = 5) 
        
#        print "\t \t end test on duration parsing"
#        pass


        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIcalParser))
    return suite

if __name__ == "__main__":
    unittest.main()
    
