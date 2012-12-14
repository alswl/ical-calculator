# -*- coding:utf-8 -*-
"""
Created on Jul 13, 2012

@author: Oberron
"""

from test_vect import testvectors, testvector_path #@UnresolvedImport
import filecmp
import sys
sys.path.append("../../src/") #to overide previous installs
import ical #@UnresolvedImport


def Run_Test_Vectors():
    print "entering test vectors"
    vect_index = 0
    for vect in testvectors[0:]:
        vect_index +=1
#        print vect
        [locfile,start,end,reference] = vect
        #print "file is:\t",file
        mycal = ical.ics(start,end)
        mycal.debug(False,"../../out/log.txt")
        mycal.local_load(testvector_path+locfile)
        mycal.parse_loaded()
        mycal.flatten()
        dates = sorted(mycal.flat_events)
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
    mycal = ical.ics("20120101","20121231")
    print "ical module: ",mycal.version
    del mycal


def see():
    print "Entering see"
    useTestVect = True
    if useTestVect:
        [locfile,start,end,reference] = testvectors[17] #@UnusedVariable
        locfile=testvector_path+locfile
    else:
        [locfile,start,end,reference] = ["C:/perso/Dropbox/entolusis/1-annum/www/ics/Calendrier_Scolaire_Zones_A_B_C_2008_2013.ics","20100101","20141231","france_doi_2007.txt"] #@UnusedVariable
#        locfile=testvector_path+locfile
#        [locfile,start,end,reference] = ["soldes_FR.ics","20100101","20141231","soldes_FR.txt"] #@UnusedVariable
    mycal = ical.ics(start,end)
    mycal.debug(True,LogPath="../../out/log.txt",debug_level=0)
    #mycal.local_load(testvector_path+file)
#    string = open(testvector_path+file,'r').readlines()

    mycal.local_load(locfile)

    mycal.parse_loaded()
    mycal.flatten()
    dates = sorted(mycal.flat_events)
    print "ics file is",locfile
    print "dates are",dates
    for event in dates:
        [date,info,uid] = event
        print date.strftime("%Y%m%d-%a")+" cw:"+str(date.isocalendar()[1])+" :\t"+info+"\t, "+uid+""
    mycal = ical.ics("20120101","20121231")
    print "ical module: ",mycal.version
    del mycal


#see()
Run_Test_Vectors()