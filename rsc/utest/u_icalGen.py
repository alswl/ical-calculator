'''
Created on Jan 2, 2013

@author: Oberron
'''
import unittest
import filecmp
import sys,datetime
sys.path.append("../../src/") #to overide previous installs
import icalendar #@UnresolvedImport
from test_vect import rrule_vects, testvector_path #@UnresolvedImport


class TestIcalGen(unittest.TestCase):
    def setUp(self):
        self.mycal = icalendar.ics()
        pass

    def tearDown(self):
        pass

    def test_RRULEgen(self):
#        print "testing RRULE gen"
        self.mycal.debug(True,LogPath="../../out/log.txt",debug_level=0)
        cal = rrule_vects[13]
#        [locfile,start,end,reference] = ["12.ics","20110101","20121231","12OL.txt"]
        [locfile,start,end,reference] = cal
        
        self.mycal.local_load(testvector_path + locfile)
        self.mycal.parse_loaded()
#        print self.mycal.events
        sRRULE = self.mycal.GenRRULEstr(self.mycal.events[0]["RRULE"])
        assert sRRULE == "RRULE:FREQ=DAILY;INTERVAL=1"
#        print "\t \t end test on RRULEgen"

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIcalGen))
    return suite

if __name__ == "__main__":
    unittest.main()
    
