'''
Created on 2013/1/3

@author: Oberron
'''
import unittest
import filecmp
import sys,datetime
sys.path.append("../../src/") #to overide previous installs
import ical #@UnresolvedImport
from test_vect import rrule_vects, testvector_path #@UnresolvedImport


class TestvEVENTParser(unittest.TestCase):

    def setUp(self):
        self.mycal = ical.ics()
        self.vevent = ical.vevent()
        pass

    def tearDown(self):
        pass
        
    def test_uid_load(self):
        vevent_load = { "uid": self.vevent.string_load}
        line = "UID:test"
        try:
            res = vevent_load["uid2"]("UID:test")
        except KeyError:
            line = line.split(":")[1]
            res = self.vevent.string_load(line)
        res = ["UID",res]
        assert res == ["UID","test"]
        
    def test_veventParse(self):
        lv = self.mycal._addEvent(["UID:uidtest","UID2:uidtest2","SUMMARY:summtest","DTSTART:20120101","DTSTAMP:20120101"])
        self.assertItemsEqual( lv , {'DTSTAMP': datetime.datetime(2012, 1, 1, 0, 0), 'UID2': 'uidtest2', 'UID': 'uidtest', 'SUMMARY': 'summtest', 'DTEND': datetime.datetime(2012, 1, 1, 0, 0), 'DTSTART': datetime.datetime(2012, 1, 1, 0, 0)})
        lv=self.mycal._addEvent(["UID:uidtest","SUMMARY:summtest","DTSTART:20120101","DTSTAMP:20120101","DURATION:P15DT5H0M20S"])
        self.assertItemsEqual(lv,{'DTSTAMP': datetime.datetime(2012, 1, 1, 0, 0), 'UID': 'uidtest', 'SUMMARY': 'summtest', 'DURATION': datetime.timedelta(5, 18020), 'DTEND': datetime.datetime(2012, 1, 6, 5, 0, 20), 'DTSTART': datetime.datetime(2012, 1, 1, 0, 0)})
        lv=self.mycal._addEvent(["UID:uidtest","SUMMARY:summtest","DTSTART:20120101","RDATE:20120101,20120202"])
#        print lv
        self.assertItemsEqual(lv,{'RDATE': [datetime.datetime(2012, 1, 1, 0, 0), datetime.datetime(2012, 2, 2, 0, 0)], 'DTEND': datetime.datetime(2012, 1, 1, 0, 0), 'DTSTART': datetime.datetime(2012, 1, 1, 0, 0), 'UID': 'uidtest', 'SUMMARY': 'summtest'})
#        print lv

    def test_RRULEParse(self):
        lv = self.vevent.rrule_load("FREQ=YEARLY;")
        self.assertItemsEqual(lv,{'FREQ': 'YEARLY'})
        lv = self.vevent.rrule_load("RRULE:FREQ=DAILY;INTERVAL=1")
        self.assertItemsEqual(lv,{'RRULE:FREQ': 'DAILY', 'INTERVAL': 1})
        lv = self.vevent.rrule_load("FREQ=WEEKLY;INTERVAL=1;BYDAY=MO,TU,WE,TH,FR;WKST=SU")
        self.assertItemsEqual(lv,{'FREQ': 'WEEKLY', 'INTERVAL': 1, 'BYDAY': {'FR': [0], 'MO': [0], 'TU': [0], 'WE': [0], 'TH': [0]}, 'WKST': 'SU'})
        lv = self.vevent.rrule_load("RRULE:FREQ=MONTHLY;INTERVAL=1;BYMONTHDAY=1,2")
        self.assertItemsEqual(lv,{'RRULE:FREQ': 'MONTHLY', 'INTERVAL': 1, 'BYMONTHDAY': [1, 2]})
#        print lv

if __name__ == "__main__":
    unittest.main()
