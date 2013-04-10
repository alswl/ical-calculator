'''
Created on Jan 2, 2013

@author: Oberron
'''
import unittest
import filecmp
import sys,datetime
sys.path.append("../../src/") #to overide previous installs
import icalendar #@UnresolvedImport
from test_vect import rrule_vects, testvector_path,RFC5545_ical #@UnresolvedImport


class TestIcalCompute(unittest.TestCase):
    def setUp(self):
        self.mycal = icalendar.ics()
        pass


    def tearDown(self):
        pass

    def test_3_1(self):
        "line folding support"
        pass

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

    
    def test_RRULECompute(self):
#        print "entering RRULE Compute"
        vect_index = 0
        for vect in rrule_vects[0:]:
            vect_index +=1
#            print vect
            [locfile,start,end,reference] = vect
            mycal = icalendar.ics()
            mycal.debug(False,"../../out/log.txt",-2)
            mycal.local_load(testvector_path+locfile)
#            mycal.parse_loaded()
            dates = mycal.get_event_instances(start,end)
            tmp = "../../out/tmp.txt"
            res = open(tmp,'w')
            for event in  dates:
#                print event
                [date, info,uid] =event
                line = "{datetime-start: "+date.strftime("%Y%m%d")+", summary: "+info+", uid: "+uid+"}\n"
                res.write(line)
                #print line
            res.close()
            assert filecmp.cmp(tmp,testvector_path+reference,shallow = False)
            
        def test_RFC5545_3_8_5_3_bis(self):
            self.mycal.local_load("C:/sw/icalculator/rsc/utest/test_vect/SCM5545_3.8.5.3_1.ics")
            ref = open("C:/sw/icalculator/rsc/utest/test_vect/SCM5545_3.8.5.3_1.txt").read()
            dates = mycal.get_event_instances("20090101","20140101")
            assert ref == dates
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIcalCompute))
    return suite

if __name__ == "__main__":
    unittest.main()
    
