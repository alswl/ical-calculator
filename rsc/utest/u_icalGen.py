'''
Created on Jan 2, 2013

@author: Oberron
'''
import unittest
import filecmp
import sys,datetime
sys.path.append("../../src/") #to overide previous installs
import icalendar #@UnresolvedImport
from icalendar_SCM import CRLF #@UnresolvedImport
from test_vect import rrule_vects, testvector_path #@UnresolvedImport



class TestIcalGen(unittest.TestCase):
    def setUp(self):
        self.mycal = icalendar.ics()
        pass

    def tearDown(self):
        pass

    def test_RRULEgen(self):
        self.mycal.debug(True,LogPath="../../out/log.txt",debug_level=0)
        cal = rrule_vects[34]
#        [locfile,start,end,reference] = ["12.ics","20110101","20121231","12OL.txt"]
        [locfile,start,end,reference] = cal
        
        self.mycal.local_load(testvector_path + locfile)
        res = self.mycal.parse_loaded()
        sRRULE = self.mycal.GenRRULEstr(self.mycal.events[0]["RRULE"]["val"])
        assert sRRULE == "RRULE:FREQ=YEARLY;INTERVAL=1"

    def test_icalGenFromLoad(self):
        self.mycal.debug(True,"c:/sw/icalculator/out/log.txt",0)
        self.mycal.local_load("c:/sw/icalculator/rsc/utest/test_vect/RFC5545/RFC5545_3.6.ics")
        self.mycal.conformance = True
        self.mycal.parse_loaded()
        res = "BEGIN:VCALENDAR"+CRLF+"VERSION:2.0"+CRLF+"PRODID:1-annum"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTAMP:20110820"+CRLF+"DTSTART:20080229"+CRLF+"UID:UID_1annum"+CRLF+"SUMMARY:29 fevrier"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF
        res2 = self.mycal.Gen_iCalendar()
#        print res2,res
#        print len(res),len(res2)
#        lenc=159
#        assert res == res2

        self.mycal.local_load("c:/sw/icalculator/rsc/utest/test_vect/RFC5545/RFC5545_3.1_3.ics")
        self.mycal.conformance=True
        self.mycal.parse_loaded()
#        print "mycal.events:",self.mycal.events
        res = "BEGIN:VCALENDAR"+CRLF+"VERSION:2.0"+CRLF+"PRODID:1-annum"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTAMP:20110820"+CRLF+"DTSTART:20080229"+CRLF+"UID:UID_1annum"+CRLF+"SUMMARY:29 fevrier"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF
        res2 = self.mycal.Gen_iCalendar()
#        print res2
#        assert res == res2

    def test_icalGenFromCode(self):
        dtstart = datetime.datetime(year=2012,month=1,day=26,hour=8,minute=12,second=10)
        dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
        rescal = "BEGIN:VCALENDAR"+CRLF+"VERSION:2.0"+CRLF+"PRODID:1-annum.com_sponsors_pyICSParser"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTAMP:"+dtstamp+CRLF+"DTSTART:20120126T081210"+CRLF+"UID:FIXMEUID"+CRLF+"SUMMARY:test"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF
        
        summary = "test"
        self.mycal.dVCALENDAR={}
        self.mycal.events =[{"DTSTART":{"val":dtstart},"SUMMARY":summary}]
        res =  self.mycal.Gen_iCalendar()
#        print "-------------\n %s \n -----------------\n %s"%(res,rescal)
        assert res == rescal
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIcalGen))
    return suite

if __name__ == "__main__":
    unittest.main()
    
