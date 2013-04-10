'''
Created on 20 Oct 2012

@author: Oberron
'''

from test_vect import rrule_vects, testvector_path,RFC5545_ical #@UnresolvedImport
import urllib
from datetime import datetime
import filecmp, sys
import json
ical2list_url = "http://ical2list.appspot.com"
#ical2list_url="http://localhost:8080"

def gae_ical2list():
    tmp = "../../out/tmp.txt"
    for vect in rrule_vects:
        [locfile,start,end,reference] = vect
        wFreq = True
        print "file is:%s \t, start is:%s \t end is: %s"%(testvector_path+locfile,start,end)
#        ref = open(testvector_path+reference,'r').readlines()
        src = open(testvector_path+locfile,'r').read()
#        src = open("C:/sw/icalculator/rsc/utest/test_vect/RFC5545/RFC5545_3.6.ics").read()

        params = {}
        params['start'] = start
        params['end'] = end
        params['snippet'] = src
        params['url'] = ""
        params['file'] = ""        
        params = urllib.urlencode(params)
#        f = urllib.urlopen("http://localhost:8085/load", params)
        f = urllib.urlopen(ical2list_url+"/load", params)
        res=f.read()
#        print "src is:",src
        print "res is:",res
        jres = json.loads(res,"utf-8")
        tmpf = open(tmp,'w')
        line =""
        for reso in jres:
            dstart = datetime.strptime(reso[0][0:10],"%Y-%m-%d")
            sstart = dstart.strftime("%Y%m%d")
            summary = reso[1]
            uid=reso[2]
            line += "{datetime-start: "+sstart+", summary: "+summary+", uid: "+uid+"}\n"
        tmpf.write(line)
        tmpf.close()
        if filecmp.cmp(tmp,testvector_path+reference,shallow = False):
            print vect,"\t - OK"
        else:
            print vect,"\t - NOK"
            sys.exit()

gae_ical2list()