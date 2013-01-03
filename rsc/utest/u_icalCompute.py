'''
Created on Jan 2, 2013

@author: Oberron
'''
import unittest
import filecmp
import sys,datetime
sys.path.append("../../src/") #to overide previous installs
import ical #@UnresolvedImport
from test_vect import rrule_vects, testvector_path #@UnresolvedImport


class TestIcalCompute(unittest.TestCase):
    def setUp(self):
        self.mycal = ical.ics()
        pass


    def tearDown(self):
        pass

    def test_RRULECompute(self):
#        print "entering RRULE Compute"
        vect_index = 0
        for vect in rrule_vects[0:]:
            vect_index +=1
#            print vect
            [locfile,start,end,reference] = vect
            mycal = ical.ics()
            mycal.debug(False,"../../out/log.txt",-2)
            mycal.local_load(testvector_path+locfile)
            mycal.parse_loaded()
            dates = mycal.get_event_instances(start,end)
            tmp = "../../out/tmp.txt"
            res = open(tmp,'w')
            for event in  dates:
                [date, info,uid] =event
                line = "{datetime-start: "+date.strftime("%Y%m%d")+", summary: "+info+", uid: "+uid+"}\n"
                res.write(line)
                #print line
            res.close()
            assert filecmp.cmp(tmp,testvector_path+reference,shallow = False)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestIcalCompute))
    return suite

if __name__ == "__main__":
    unittest.main()
    
