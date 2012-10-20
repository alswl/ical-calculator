'''
Created on 20 Oct 2012

@author: matt_2
'''
from test_vect import testvectors,testvector_path
import urllib
import filecmp, sys

def gae_ical2list():
    tmp = "../../out/tmp.txt"
    for cal in testvectors[5:6]:
        [file,start,end,reference] = cal
        wFreq = True
#        print "file is:\t",file,"start is:",datetime.datetime.strftime(datetime.datetime.strptime(start,"%Y%m%d"),"%Y%m%d-%a"),"end is:",end
        ref = open(testvector_path+reference,'r').readlines()
        src = open(testvector_path+file,'r').read()
        params = {}
        params['start'] = start
        params['end'] = end
        params['content'] = src
        params['url'] = ""
        params['file'] = ""
        
        params = urllib.urlencode(params)
        f = urllib.urlopen("http://ical2list.appspot.com/load", params)
        res=f.read()
        tmpf = open(tmp,'w')
        line =""
        for reso in res:
            print res[0], res[1]
#                    print "reso",reso,start,end
#            if reso<=end and reso>=start:
#                line += "{datetime-start: "+reso.strftime("%Y%m%d")+", summary: "+str(event[3])+", uid: "+event[4]+"}\n"
#                        print "line is",line.replace("\n","")
        tmpf.write(line)
        tmpf.close()
        if filecmp.cmp(tmp,testvector_path+reference,shallow = False):
            print cal,"\t - OK"
        else:
            print cal,"\t - NOK"
            sys.exit()

gae_ical2list()