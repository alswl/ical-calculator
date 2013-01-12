# -*- coding:utf-8 -*-
"""
Created on Apr 10, 2012

@version: 0.2: all tests passed
old: 0.1 up to 150l.ics - ok

@todo: need to fix the soldes_FR item, the rest works (in test_vect.version == "0.2"
@author: Oberron
"""
import datetime
import filecmp, sys
from dateutil.rrule import *
from dateutil.parser import *
from test_vect import testvectors,testvector_path #@UnresolvedImport
import icalendar #@UnresolvedImport

version = "0.2"

_freq_map = {"YEARLY": YEARLY,
             "MONTHLY": MONTHLY,
             "WEEKLY": WEEKLY,
             "DAILY": DAILY,
             "HOURLY": HOURLY,
             "MINUTELY": MINUTELY,
             "SECONDLY": SECONDLY}

_weekday_map = {"MO":0,"TU":1,"WE":2,"TH":3,"FR":4,"SA":5,"SU":6}


class dow(object):
    __slots__ = ["weekday", "n"]
    def __call__(self, n):
        if n == self.n:
            return self
        else:
            return self.__class__(self.weekday, n)

    def __init__(self, weekday, n=None):
        if n == 0:
            raise ValueError, "Can't create weekday with n == 0"
        self.weekday = weekday
        self.n = n

    def __repr2__(self):
        s = ("MOa", "TUa", "WEa", "THa", "FRa", "SAa", "SUa")[self.weekday]
        if not self.n:
            return s
        else:
            return "%s(%+d)" % (s, self.n)

    
def test_rrule_import():
    year = rrule(YEARLY,bymonth=8,bymonthday=13,byweekday=FR)[0].year
    dates = rrule(YEARLY,bymonth=8,bymonthday=13,byweekday=FR)
    print "Year with next Aug 13th on a Friday is:", year
    for date in dates:
        print "list of dates",date

def unit_test_rrule():
    """ testing the matching between dateutils icalendar rrule enumerator and own one """
    for cal in testvectors[5:]:
        [file,start,end,reference] = cal
        wFreq = True
        mycal = icalendar.ics(start,end)
#        print "file is:\t",file,"start is:",datetime.datetime.strftime(datetime.datetime.strptime(start,"%Y%m%d"),"%Y%m%d-%a"),"end is:",end
        ref = open(testvector_path+reference,'r').readlines()
        mycal.debug(False,"C:/sw/ical2xcal/out/log.txt")
        mycal.local_load(testvector_path+file)
        mycal.parse_loaded()
        end = datetime.datetime.strptime(end,"%Y%m%d")
        start = datetime.datetime.strptime(start,"%Y%m%d")
        for event in mycal.events:
            wbyday = False
#            print "event is:\t",event
            tmp = "../../out/tmp.txt"
            frequence = None
            count_= None
            interval_ = 1
            until_ = None
            byweekday_ = None
            bymonth_=None
            bysetpos_=None
            wkst_ = None
            bymonthday_ = None
            byyearday_ = None
            byweekno_ = None
#            print "event[2]:",event[2]
            if "FREQ" in event[2]:
                frequence = _freq_map[event[2]["FREQ"]]
#                print "frequence",frequence
                count_ = None
                if "COUNT" in event[2]:
                    count_ = event[2]["COUNT"]
                if "BYWEEKNO" in event[2]:
                    byweekno_ = tuple(event[2]["BYWEEKNO"])
                if "BYYEARDAY" in event[2]:
                    byyearday_ = tuple(event[2]["BYYEARDAY"])
                if "INTERVAL" in event[2]:
                    interval_ = event[2]["INTERVAL"]
                if "BYMONTH" in event[2]:
                    bymonth_=event[2]["BYMONTH"]
                if "BYSETPOS" in event[2]:
                    bysetpos_=event[2]["BYSETPOS"]
                if "UNTIL" in event[2]:
                    until_ = event[2]["UNTIL"]
                if "WKST" in event[2]:
                    wkst_ = dow(_weekday_map[event[2]["WKST"]])
                if "BYDAY" in event[2]:
                    byweekday_ =[]
                    wbyday=True
#                    print event[2]["BYDAY"]
                    for wd in event[2]["BYDAY"]:
#                        print "wd, map",wd,_weekday_map[wd]
#                        print "log 106",wd,event[2]["BYDAY"][wd]
                        for wodi in event[2]["BYDAY"][wd]:
                            if wodi==0:
                                byweekday_.append(dow(_weekday_map[wd]))
                            else:
#                                print "log 110",event[2]["BYDAY"][wd],"wodi",wodi
                                byweekday_.append(dow(_weekday_map[wd])(wodi)) # event[2]["BYDAY"]
                    byweekday_ = tuple(byweekday_)                        
                if "BYMONTHDAY" in event[2]:
                    bymonthday_ = tuple(event[2]["BYMONTHDAY"])
#                print "rrule parameters: ",event[2], "freq:",frequence, "dtstart",event[0]
                #byweekday_ = (MO(1),MO(2))
#                byweekday_ = (MO(1))
                res = rrule(frequence,count = count_,dtstart=event[0],interval=interval_, byweekday=byweekday_,bymonth=bymonth_,bysetpos=bysetpos_, wkst= wkst_,bymonthday=bymonthday_, until = until_,byyearday =byyearday_, byweekno = byweekno_)
#                print "end rrule processing"
                #TODO: intersect res with start / end
                res = sorted(res)
                tmpf = open(tmp,'w')
                line =""
                for reso in res:
#                    print "reso",reso,start,end
                    if reso<=end and reso>=start:
                        line += "{datetime-start: "+reso.strftime("%Y%m%d")+", summary: "+str(event[3])+", uid: "+event[4]+"}\n"
#                        print "line is",line.replace("\n","")
                tmpf.write(line)
                tmpf.close()
            else:
                print "\t no FREQ properties"
                wFreq = False
        if wFreq:
            mycal.flatten()
            dates = sorted(mycal.flat_events)
            if filecmp.cmp(tmp,testvector_path+reference,shallow = False):
                print cal,"\t - OK"
            else:
                print cal,"\t - NOK"
                sys.exit()
        else:
            print "\t *****some event w/o FREQ"
    #        sys.exit()

def see():
    print "Entering see"
#    useTestVect = False
    [file,start,end,reference] = testvectors[4]
    mycal = icalendar.ics(start,end)
    ref = open(testvector_path+reference,'r').readlines()

    mycal.debug(False,"C:/sw/ical2xcal/out/log.txt")
    mycal.local_load(testvector_path+file)
    mycal.parse_loaded()
    mycal.flatten()
    dates = sorted(mycal.flat_events)
    index = 0
    for event in dates:
        [date,info,uid] = event
#        print date.strftime("%Y%m%d-%a")+" cw:"+str(date.isocalendar()[1])+" :\t"+info+"\t, "+uid+""
        print date,info,uid
        print "\t"+ref[index]
        index+=1


#test_weekday()
#see()
unit_test_rrule()
#test_rrule_import()