# -*- coding:utf-8 -*-
"""
Created on Jul 28, 2011

@author: Oberron
@attention: http://www.calconnect.org/tests/iCalendar-RRULE-Interop/iCalendar-RRULE-Interop-Matrix.html
@attention:http://www.calconnect.org/tests/recurr_ical_streams.doc
"""
import ical
import filecmp
import sys

testvector_path = "../rsc/test_vect/"

testvectors = [
               ["by_ferie.ics","20110101","20121231","by_ferie_res.txt"],
               ["rdate.ics","20110101","20121231","rdate.txt"],
               ["Ferien_Bayern_2012.ics","20110101","20121231","Ferien_Bayern_2012.txt"],
               ["deutschland.ics","20110101","20121231","deutschland.txt"],
               
               ["anmar1.ics","20050101","20051231","anmar1.txt"],
               ["anmar2.ics","20050101","20051231","anmar2.txt"],
               ["anmar3.ics","20050101","20051231","anmar3.txt"],
               ["anmar4.ics","20050101","20051231","anmar4.txt"],
               ["anmar5.ics","20050101","20051231","anmar5.txt"],
               ["anmar6.ics","20050101","20051231","anmar6.txt"],
               ["anmar7.ics","20050101","20051231","anmar7.txt"],
               ["anmar8.ics","20050101","20051231","anmar8.txt"],
               ["anmar9.ics","20050101","20051231","anmar9.txt"],
               
               
               ["calconnect/ical/01.ics","20110101","20121231","calconnect/ical/01.txt"],
               ["calconnect/ical/02.ics","20110101","20121231","calconnect/ical/02.txt"],
               ["calconnect/ical/03.ics","20110101","20121231","calconnect/ical/03.txt"],
               
               ["16ZB.ics","20110101","20121231","16ZB.txt"],
               ["15OL.ics","20110101","20121231","15OL.txt"],
               ["14OL.ics","20110101","20121231","14OL.txt"],
               ["13ZB.ics","20110101","20121231","13ZB.txt"],
               ["13OL.ics","20110101","20121231","13OL.txt"],
               ["13IC.ics","20110101","20121231","13IC.txt"],
               ["13MO.ics","20110101","20121231","13MO.txt"],
               ["12ZB.ics","20110101","20121231","12ZB.txt"],
               ["12OL.ics","20110101","20121231","12OL.txt"],
               ["12IC.ics","20110101","20121231","12IC.txt"],
               ["12MO.ics","20110101","20121231","12MO.txt"],
               ["10MO.ics","20110101","20121231","10MO.txt"],
               ["10OL.ics","20110101","20121231","10OL.txt"],

               ["php0a.ics","19960101","20001231","php0a.txt"],
               ["php0b.ics","19960101","20001231","php0b.txt"],
               ["php0c.ics","19960101","20001231","php0c.txt"],
               ["php0d.ics","19960101","20001231","php0d.txt"],
               ["php0e.ics","19960101","20011231","php0e.txt"],

               ["php2a.ics","19960101","20011231","php2a.txt"],
               ["php2b.ics","19960101","20011231","php2b.txt"],
               ["php2c.ics","19960101","20011231","php2c.txt"],
               ["php2d.ics","19960101","20121231","php2d.txt"],
               ["php2e.ics","19960101","20121231","php2e.txt"],
               ["php2f.ics","19960101","20121231","php2f.txt"],

               ["php3a.ics","19960101","20011231","php3a.txt"],
               ["php3b.ics","19960101","20011231","php3b.txt"],
               ["php3c.ics","19960101","20011231","php3c.txt"],
               ["php3d.ics","19960101","20011231","php3d.txt"],
               ["php3e.ics","19960101","20011231","php3e.txt"],
               ["php3f.ics","19960101","20011231","php3f.txt"],

               ["php4a.ics","19960101","20011231","php4a.txt"],
               ["php4b.ics","19960101","20011231","php4b.txt"],
               ["php4c.ics","19960101","20011231","php4c.txt"],
               ["php4d.ics","19960101","20011231","php4d.txt"],
               ["php4e.ics","19960101","20011231","php4e.txt"],
               ["php4f.ics","19960101","20121231","php4f.txt"],

               ["php5a.ics","19960101","20121231","php5a.txt"],
               ["php5b.ics","19960101","20121231","php5b.txt"],
               ["php5c.ics","19960101","20121231","php5c.txt"],
               ["php5d.ics","19960101","20121231","php5d.txt"],
               ["php5e.ics","19960101","20121231","php5e.txt"],
               ["php5f.ics","19960101","20121231","php5f.txt"],

               ["wkst0.ics","19960101","20011231","wkst0.txt"],
               ["wkst1.ics","19960101","20011231","wkst1.txt"],
               ["29fev.ics","20080101","20121231","29fev.txt"]]

def Run_Test_Vectors():
    print "entering test vectors"
    for vect in testvectors:
        [file,start,end,reference] = vect
        #print "file is:\t",file
        mycal = ical.ics(start,end)
        mycal.debug(False,"C:/sw/ical2xcal/out/log.txt")
        mycal.local_load(testvector_path+file)
        mycal.parse_loaded()
        mycal.flatten()
        dates = sorted(mycal.flat_events)
        tmp = "../out/tmp.txt"
        res = open(tmp,'w')
        for event in  dates:
            [date, info,uid] =event
            line = date.strftime("%Y%m%d")+":\t"+info+"\n"
            res.write(line)
            #print line
        res.close()
        if filecmp.cmp(tmp,testvector_path+reference,shallow = False):
            print vect,"\t - OK"
        else:
            print vect,"\t - NOK"
            sys.exit()
        del mycal


def see():
    print "Entering see"
    useTestVect = True
    if useTestVect:
        [file,start,end,reference] = testvectors[-1]
    else:
        [file,start,end,reference] = ["u2012.ics","20120101","20121231","u2012.txt"]        
    mycal = ical.ics(start,end)
    mycal.debug(True,LogPath="e:/sw/ics2json/out/log.txt",debug_level=0)
    #mycal.local_load(testvector_path+file)
    string = open(testvector_path+file,'r').readlines()

    mycal.local_load(testvector_path+file,'r')

    mycal.parse_loaded()
    mycal.flatten()
    dates = sorted(mycal.flat_events)
    print "ics file is",file
    print "dates are",dates
    print 'mycal is',mycal.ical_data
    
    for event in dates:
        [date,info,uid] = event
        print date.strftime("%Y%m%d-%a")+" cw:"+str(date.isocalendar()[1])+" :\t"+info+"\t, "+uid+""

log = open('e:\sw\ics2json\out\log2.txt','w')
log.write('test')
log.close()

see()
#Run_Test_Vectors()          