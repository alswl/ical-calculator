'''
Created on 20 Oct 2012

@author: Oberron
'''

from test_vect import testvectors,testvector_path #@UnresolvedImport
import urllib
from datetime import datetime
import filecmp, sys
import json

def gae_ical2list():
    tmp = "../../out/tmp.txt"
    for cal in testvectors:
        [file,start,end,reference] = cal
        wFreq = True
#        print "file is:\t",file,"start is:",datetime.datetime.strftime(datetime.datetime.strptime(start,"%Y%m%d"),"%Y%m%d-%a"),"end is:",end
        ref = open(testvector_path+reference,'r').readlines()
        src = open(testvector_path+file,'r').read()
        params = {}
        params['start'] = start
        params['end'] = end
        params['snippet'] = src
        params['url'] = ""
        params['file'] = ""        
        params = urllib.urlencode(params)
#        f = urllib.urlopen("http://localhost:8085/load", params)
        f = urllib.urlopen("http://ical2list.appspot.com/load", params)
        res=f.read()
#        print res
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
            print cal,"\t - OK"
        else:
            print cal,"\t - NOK"
            sys.exit()

gae_ical2list()