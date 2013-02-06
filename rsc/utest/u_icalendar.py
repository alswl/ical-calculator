# -*- coding:utf-8 -*-
"""
Created on Jul 13, 2012

all ok with * icalendar "0.6.1y1" and test_vect "0.3"

@author: Oberron
"""

from test_vect import rrule_vects, testvector_path #@UnresolvedImport
import filecmp
import sys
sys.path.append("../../src/") #to overide previous installs
import icalendar #@UnresolvedImport


def Run_Test_Vectors():
    """ testing the icalendar module parser and enumerator """
    print "entering test vectors"
    vect_index = 0
    for vect in rrule_vects:
        print vect
        [locfile,start,end,reference] = vect
        #print "file is:\t",file
        mycal = icalendar.ics()
        mycal.debug(False,"../../out/log.txt",-2)
        mycal.local_load(testvector_path+locfile)
#        mycal.parse_loaded()
        dates = mycal.get_event_instances(start,end)
#        mycal = ical.ics(start,end)
#        mycal.debug(False,"../../out/log.txt")
#        mycal.local_load(testvector_path+locfile)
#        mycal.parse_loaded()
#        mycal.flatten()
#        dates = sorted(mycal.flat_events)
        tmp = "../../out/tmp.txt"
        res = open(tmp,'w')
        for event in  dates:
            [date, info,uid] =event
            line = "{datetime-start: "+date.strftime("%Y%m%d")+", summary: "+info+", uid: "+uid+"}\n"
            res.write(line)
            #print line
        res.close()
        if filecmp.cmp(tmp,testvector_path+reference,shallow = False):
            print vect_index,":",vect,"\t - OK"
        else:
            print vect_index,":",vect,"\t - NOK"
            sys.exit()
        del mycal
        vect_index +=1
    mycal = icalendar.ics()
    print "ical module: ",mycal.version
    del mycal


def see(index=-1):
    print "Entering see"
    logpath = "../../out/log.txt"
    useTestVect = True
    if useTestVect:
        [locfile,start,end,reference] = rrule_vects[index] #@UnusedVariable
        locfile=testvector_path+locfile
    else:
        [locfile,start,end,reference] = ["C:/perso/Dropbox/entolusis/1-annum/www/ics/Calendrier_Scolaire_Zones_A_B_C_2008_2013.ics","20100101","20141231","france_doi_2007.txt"] #@UnusedVariable
#        locfile=testvector_path+locfile
#        [locfile,start,end,reference] = ["soldes_FR.ics","20100101","20141231","soldes_FR.txt"] #@UnusedVariable
    mycal = icalendar.ics()
    mycal.debug(True,LogPath="",debug_level=0)
    #mycal.local_load(testvector_path+file)
#    string = open(testvector_path+file,'r').readlines()

    mycal.local_load(locfile)
#    mycal.parse_loaded()
#    mycal.flatten()
    dates = mycal.get_event_instances(start, end)
    print "ics file is",locfile
    print "time window is from %s - to:%s"%(start,end)
    print "dates are",dates
    for event in dates:
        [date,info,uid] = event
        print date.strftime("%Y%m%d-%a")+" cw:"+str(date.isocalendar()[1])+" :\t"+info+"\t, "+uid+""
#    mycal = icalendar.ics()
    print "ical module: ",mycal.version
    log = open(logpath,'w')
    log.write(mycal.LogData)
    log.close()
    del mycal


def t2():
    log = open("c:/sw/icalculator/out/log.txt",'w')
    log.write(" ")
    log.close()
    vect_index = 0
    for vect in rrule_vects[0:]:
        vect_index +=1
#            print vect
        [locfile,start,end,reference] = vect
        print "file is:\t",locfile,reference
        mycal = icalendar.ics()
        mycal.debug(False,"../../out/log.txt",-2)
        mycal.local_load(testvector_path+locfile)
        mycal.parse_loaded()
        dates = mycal.get_event_instances(start,end)
#        print dates
        tmp = "../../out/tmp.txt"
        res = open(tmp,'w')
        for event in  dates:
            [date, info,uid] =event
            line = "{datetime-start: "+date.strftime("%Y%m%d")+", summary: "+info+", uid: "+uid+"}\n"
            res.write(line)
            #print line
        res.close()
        if filecmp.cmp(tmp,testvector_path+reference,shallow = False):
            print vect_index,":",vect,"\t - OK"
        else:
            print vect_index,":",vect,"\t - NOK"
#            sys.exit()
        del mycal


#t2()
#see(81)
Run_Test_Vectors()