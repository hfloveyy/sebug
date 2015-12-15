#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup
import re
from dummy import *
import cPickle as pickle
names = {}
urls = []
def get_url():
    for i in range(55,100):
        url = 'https://www.sebug.net/vuldb/ssvid-'+str(i)
        urls.append(url)
    return urls

def get_title(data): 
    soup = BeautifulSoup(data,"html.parser")
    for string in soup.strings:
        if 'CVE-20' in string: 
            break 
        else:
            title = soup.h1.string.encode('utf-8').strip()
            ssv = soup.find(href=re.compile("/help/vul#ssv")).string
            names[title] = title
            names[ssv] = ssv
            break




 

if __name__ == '__main__':
    get_url()
    for url in  urls:
        code, head,data, errcode, _ = curl.curl2(url) 
        if code==200:
            get_title(data)
    file_sebug = file('sebug.txt','w+')
    for title,ssv in names.items():
        print title+'   '+ssv
        file_sebug.writelines(title+'  '+ssv)







