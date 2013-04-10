# -*- coding:utf-8 -*-
'''
Created on Nov 27, 2012

@author: Oberron
'''
import unittest
import filecmp
import sys,datetime
sys.path.append("../../src/") #to overide previous installs
import icalendar #@UnresolvedImport
from test_vect import rrule_vects, testvector_path,SCM_withWildICS #@UnresolvedImport
from icalendar_SCM import RFC5545_SCM #@UnresolvedImport

overall_conformance = False

class TestIcalParser(unittest.TestCase):

    def setUp(self):
        self.mycal = icalendar.ics()
        self.vevent = icalendar.vevent()
        self.TZ = icalendar.newTZinfo()

        pass

    def tearDown(self):
        pass
    
    def test_3_1(self):
        "line folding support"
        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/SCM5545_3.1_1.ics")
        self.mycal.parse_loaded()
#        print self.mycal.dSCM
        assert {9: ['3.1_2']} == self.mycal.dSCM
        assert self.mycal.events[0]["UID"]["val"] == "SCM3_1"
        assert self.mycal.events[0]["DTSTART"]["val"] == datetime.datetime(2013,2,24,19)

    def test_3_1_1(self):
        "test the list separators"
        pass

    def test_3_1_2(self):
        "test the ability to get all values for properties with multiple values"
        pass

    def test_3_1_3(self):
        "binary value"
        pass

    def test_3_1_4(self):
        "character set - need to come-up with relevant test + appropriate method"
        pass

        
    def test_SCM5545_3_8_5_3(self):
        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/SCM5545_3.8.5.3_1.ics")
        self.mycal.parse_loaded()
        assert "3.8.5.3_1" in self.mycal.lSCM
        
    def test_SCM5545_3_6_1v2(self):
        self.mycal.lSCM = []
        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/SCM5545_3.6.1_2.ics")
#        self.mycal.conformance = True
        self.mycal.parse_loaded()
#        print "line 34:",self.mycal.lSCM
        assert "3.6.1_2" in self.mycal.lSCM
        self.mycal.lSCM = []
        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/SCM5545_3.6.1_2a.ics")
#        self.mycal.conformance = True
        self.mycal.parse_loaded()
#        print "line 34:",self.mycal.lSCM
        assert "3.6.1_2" in self.mycal.lSCM
        
        
    def test_3_8_4_7_1_UID(self):
#        print "test "+ "3.8.4.7_1"
        self.mycal.lSCM = []
        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/RFC5545/SCM5545_3.8.4.7_1.ics")
#        self.mycal.conformance = True
        self.mycal.parse_loaded()
#        print "line 34:",self.mycal.lSCM
        assert "3.8.4.7_1" in self.mycal.lSCM
        
    def test_Duration_fromRFC2445(self):
#        print "testing Duration parsing"
#        mycal = icalendar.ics()
        """RFC2445 p37
        Example: A duration of 15 days, 5 hours and 20 seconds would be:
        P15DT5H0M20S
        """
        [years,months,tdelta] = self.vevent.duration_load("P15DT5H0M20S")
#        print "line 33",res, "---",datetime.timedelta(days = 15, hours = 5, seconds = 20)
        assert tdelta == datetime.timedelta(days = 15, hours = 5, seconds = 20)
        assert [years, months] == [0,0]
        """
        A duration of 7 weeks would be:
        P7W
        """
        [years,months,tdelta] = self.vevent.duration_load("P7W")
        assert tdelta == datetime.timedelta(weeks = 7) 
        assert [years, months] == [0,0]
        
        """
        The period start at 18:00:00 on January 1, 1997 and lasting 5 hours
        and 30 minutes would be:        
        19970101T180000Z/PT5H30M
        """
        [years,months,tdelta] = self.vevent.duration_load("PT5H30M")
        assert tdelta == datetime.timedelta(hours = 5, minutes=30) 
        assert [years, months] == [0,0]
        
        """
        rfc2445 p71
        15 minute 
        PT15M
        """
        [years,months,tdelta] = self.vevent.duration_load("PT15M")
        assert tdelta == datetime.timedelta(minutes=15) 
        assert [years, months] == [0,0]
        
        """
        rfc2445 p71
        30 minutes before the scheduled start of the event
        -PT30M
        """
        [years,months,tdelta] = self.vevent.duration_load("-PT30M")
#        print "res 61:",res
#        print datetime.timedelta(minutes = -30)
        assert tdelta == datetime.timedelta(minutes=-30) 
        assert [years, months] == [0,0]
        
        """
        rfc2445 p72
        one hour intervals
        PT1H
        """
        [years,months,tdelta] = self.vevent.duration_load("PT1H")
        assert tdelta == datetime.timedelta(hours = 1) 
        assert [years, months] == [0,0]
        
        """
        RFC2445 p94
        interval of time of 1 hour and zero minutes and zero seconds
        PT1H0M0S
        """
        [years,months,tdelta] = self.vevent.duration_load("PT1H0M0S")
        assert tdelta == datetime.timedelta(hours = 1,minutes = 0, seconds =0) 
        assert [years, months] == [0,0]
        
        """
        rfc2445 p126
        with a 5 minute delay
        PT5M
        """
        [years,months,tdelta] = self.vevent.duration_load("PT5M")
        assert tdelta == datetime.timedelta(minutes = 5) 
        assert [years, months] == [0,0]
        
#        print "\t \t end test on duration parsing"
#        pass

    def test_Duration_fromRFC5545(self):
        
        """
        p74:
        DURATION:PT15M
        15-minute
        """
        [years,months,tdelta] = self.vevent.duration_load("PT15M")
        assert tdelta == datetime.timedelta(minutes = 15)
        assert [years, months] == [0,0]
        
        """
        p98:
        DURATION:PT1H0M0S
        one hour and zero minutes and zero seconds:
        """ 
        [years,months,tdelta] = self.vevent.duration_load("PT1H0M0S")
        assert tdelta == datetime.timedelta(hours = 1, minutes =0, seconds = 0)
        assert [years, months] == [0,0]
        
        """
        p145
        DURATION:PT1H
        one hour
        """
        [years,months,tdelta] = self.vevent.duration_load("PT1H")
        assert tdelta == datetime.timedelta(hours = 1)
        assert [years, months] == [0,0]
        
        """
        p34
        Note that unlike [ISO.8601.2004], this value type doesn't support the "Y" and "M"
        designators to specify durations in terms of years and months.
        """
        [years,months,tdelta] = self.vevent.duration_load("P1Y")
#        print self.mycal.lSCM, self.mycal.vevent.lSCM
        assert "3.3.6_1" in self.vevent.lSCM
        assert tdelta == datetime.timedelta (days = 0)
        assert [years, months] == [1,0]
        
        [years,months,tdelta] = self.vevent.duration_load("P1M")
        assert "3.3.6_1" in self.vevent.lSCM
        assert tdelta == datetime.timedelta (days = 0)
        assert [years, months] == [0,1]


    def test_RFC5545_3_8_2_4(self):
        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/RFC5545/RFC5545_3.8.2.4_1.ics")
        self.mycal.conformance = overall_conformance
        self.mycal.parse_loaded()
#        print "line 183:",self.mycal.lSCM
        assert "3.8.2.4_1" in self.mycal.lSCM
        
        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/RFC5545/RFC5545_3.8.2.4_2.ics")
        self.mycal.conformance = overall_conformance
        self.mycal.parse_loaded()
#        print "line 189",self.mycal.lSCM,self.mycal.dVCALENDAR
#        print "line 190",self.mycal.lSCM
        assert '3.8.2.4_2' in self.mycal.lSCM

        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/RFC5545/RFC5545_3.6.1_0.ics")
        self.mycal.conformance = overall_conformance        
        self.mycal.parse_loaded()
#        print "line 195",self.mycal.lSCM
        assert '3.6.1_0' in self.mycal.lSCM

        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/RFC5545/RFC5545_3.6.1_0a.ics")
        self.mycal.conformance = overall_conformance        
        self.mycal.parse_loaded()
#        print "line 202",self.mycal.lSCM,self.mycal.events
        assert '3.6.1_0' in self.mycal.lSCM

    def test_METHOD_presence(self):
        self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/anmar1.ics")
        self.mycal.parse_loaded()
        assert "METHOD" in self.mycal.dVCALENDAR
        assert self.mycal.dVCALENDAR["METHOD"]["val"] == "REQUEST"
    
    def test_withWildICS(self):
        SCMvects = SCM_withWildICS
        index = 0
        for SCMvect in SCMvects:
            [icsfile,scm_errors]=SCMvect
#            print "..........\t %s"%icsfile
            self.mycal.lSCM = {}
            self.mycal.isCalendarFileCompliant(icsfile,_ReportNonConformance = False)
    #            print "mycal.lSCM: %s \n recorded errors: %s"%(self.mycal.lSCM,scm_errors)
            for scm_code in scm_errors:
    #                print scm_code
                try:
                    assert scm_code in self.mycal.lSCM
                except Exception,e:
#                    print "index is: %s, file is: %s"%(index,icsfile)
#                    print "scm_errors: %s \n dSCM: %s"%(scm_errors,self.mycal.dSCM)
#                    print "caught e: %s - END"%e.strerror
#                    e.strerror = e.strerror+ "file: %s"%icsfile
                    msg = "Error reporting matches failed for index/file\n%s: %s \n values were: \n*: %s \n*: %s "%(index,icsfile,scm_errors,self.mycal.dSCM)
                    raise Exception(msg)
            for scm_code in self.mycal.lSCM:
    #                print scm_code
                try:
                    assert scm_code in self.mycal.lSCM
                except Exception,e:
                    print "index is: %s, file is: %s"%(index,icsfile)
                    print "dSCM: %s \n scm_errors: %s"%(self.mycal.dSCM,scm_errors)
                    msg = "Error reporting matches failed for index/file\n%s: %s \n values were: \n*: %s \n*: %s "%(index,icsfile,scm_errors,self.mycal.dSCM)
                    raise Exception(msg)
            index +=1

    def test_DATETIME_load(self):
        folder = "C:/sw/icalculator/rsc/utest/test_vect/RFC5545/"
        ics = ["RFC5545_3.1_3.ics", "RFC5545_3.8.5.3_11.ics"]
        fileics = ics[0]
        self.mycal.local_load(folder+fileics)
        self.mycal.conformance = overall_conformance
        self.mycal.parse_loaded()
#        print "line 228",self.mycal.events[0]["DTSTAMP"]["val"].tzinfo.getID() == "UTC"
        assert self.mycal.events[0]["DTSTAMP"]["val"].tzinfo.getID() == "UTC"
        fileics = ics[1]
        self.mycal.local_load(folder+fileics)
        self.mycal.conformance = overall_conformance
        self.mycal.parse_loaded()
#        print "line 234",self.mycal.events[0]["DTSTART"]["val"].tzinfo.getID() == "America/New_York"
        assert self.mycal.events[0]["DTSTART"]["val"].tzinfo.getID() == "America/New_York"

    def test_Period_load(self):
        perval = "19970101T180000Z/19970102T070000Z"
        self.TZ.setID("UTC")
        perthres = [datetime.datetime(1997,1,1,18,0,0,tzinfo=self.TZ),datetime.datetime(year=1997,month=1,day=2,hour=7,tzinfo=self.TZ)]
        per_res = self.vevent.period_load(perval)
        self.assertEqual( perthres , per_res)

        perval = "19970101T180000Z/PT5H30M"
        per_res = self.vevent.period_load(perval)
        perthres = [datetime.datetime(1997,1,1,18,0,0,tzinfo=self.TZ),[0,0,datetime.timedelta(hours=5,minutes=30)]]
        self.assertEqual( perthres , per_res)
                
        perval = "19970308T160000Z/PT8H30M"
        per_res = self.vevent.period_load(perval)
        perthres = [datetime.datetime(1997,3,8,16,0,0,tzinfo=self.TZ),[0,0,datetime.timedelta(hours=8,minutes=30)]]
        self.assertEqual( perthres , per_res)
        
        perval = "19970308T160000Z/PT3H,19970308T200000Z/PT1H"
        per_res = self.vevent.period_load(perval)
        perthres = [[datetime.datetime(1997,3,8,16,0,0,tzinfo=self.TZ),[0,0,datetime.timedelta(hours=3,minutes=0)]],
                    [datetime.datetime(1997,3,8,20,0,0,tzinfo=self.TZ),[0,0,datetime.timedelta(hours=1,minutes=0)]]]
        self.assertEqual( perthres , per_res)
        
        perval = "19970308T160000Z/PT3H,19970308T200000Z/PT1H,19970308T230000Z/19970309T000000Z"
        per_res = self.vevent.period_load(perval)
        perthres = [[datetime.datetime(1997,3,8,16,0,0,tzinfo=self.TZ),[0,0,datetime.timedelta(hours=3,minutes=0)]],
                    [datetime.datetime(1997,3,8,20,0,0,tzinfo=self.TZ),[0,0,datetime.timedelta(hours=1,minutes=0)]],
                    [datetime.datetime(1997,3,8,23,0,0,tzinfo=self.TZ),datetime.datetime(1997,3,9,0,0,0,tzinfo=self.TZ)]
                    ]
        self.assertEqual( perthres , per_res)
        
    def test_slot_duration(self):
        slot_dur = self.mycal._get_number_slots(datetime.datetime(2013,2,5),datetime.datetime(2013,2,6),datetime.timedelta(days=1))
        assert slot_dur == 1

        slot_dur = self.mycal._get_number_slots(datetime.datetime(2013,2,5),datetime.datetime(2013,2,7),datetime.timedelta(days=1))
        assert slot_dur == 2

    def test_dtType(self):
        dttype = self.mycal._type_date(datetime.datetime(2013,2,6).date())
        assert dttype == "DATE"
        dttype = self.mycal._type_date(datetime.datetime(2000,1,1).date())
        assert dttype == "DATE"
        dttype = self.mycal._type_date(datetime.datetime(2013,2,6))
        assert dttype == "DATETIME-FLOAT"
        dttype = self.mycal._type_date(datetime.datetime(2000,1,1))
        assert dttype == "DATETIME-FLOAT"
        dttype = self.mycal._type_date(datetime.datetime(2013,2,6,tzinfo=self.TZ))
        assert dttype == "DATETIME-TZ"
        dttype = self.mycal._type_date(datetime.datetime(2000,1,1,tzinfo=self.TZ))
        assert dttype == "DATETIME-TZ"
        
        
def suite():
    print "suite"
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIcalParser))
    return suite

if __name__ == "__main__":
#    print "main"
#    all = True
    RunAll = False
    if RunAll :
        unittest.main()
    else:
        uniquetest = unittest.TestSuite()
        uniquetest.addTest(TestIcalParser('test_3_1'))
        unittest.TextTestRunner(verbosity=2).run(uniquetest)
