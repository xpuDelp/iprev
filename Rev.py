import requests
import re
from multiprocessing.dummy import Pool
import sys

import os 

# Made by t.me/sam4klo

#for ip in ips:
def revip(url):
        try:
            req = requests.get('https://api.webscan.cc/?action=query&ip='+url).text
            if '"domain":' in req:
                ree = re.findall('"domain": "(.*?)"', req)
                for r in ree:
                    dom = r.replace("'", "").replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','')
                    print(' IP: '+url+' OK')
                    open('grab.txt', 'a').write('http://'+dom+'\n')
                    
            else:
                print(' IP: '+url+' BAD')
                    
        except:
            pass

logo = """
Made by https://t.me/sam4klo, channel: https://t.me/rtaxdrops
"""
print(logo)

def main():
    list = raw_input(" Ip List :~# ")
    crownes = raw_input(" Thread :~# ")
    rev1 = open(list, 'r').read().splitlines()
    pp = Pool(int(crownes))
    pr = pp.map(revip, rev1)

if __name__ == '__main__':
	main()
