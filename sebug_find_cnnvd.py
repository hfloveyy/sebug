#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup
import re
from dummy import *
import time, threading
names = {}
urls = []
titles = []
ssvs = []
s = '0123456789'
vulurl = 'https://www.sebug.net/vuldb/ssvid-'
def get_url():
    for i in range(82000,83000):#83000
        url = 'https://www.sebug.net/vuldb/ssvid-'+str(i)
        urls.append(url)
    return urls

def get_title(data): 
    CNNVD = True 
    CVE = False
    soup = BeautifulSoup(data,"html.parser")
    for string in soup.strings:
        if 'CNNVD-20'  in string: 
            CNNVD = False
        if 'CVE-20' in string:
            CVE = True
    if CNNVD and CVE:
        title = soup.h1.string.encode('utf-8').strip()
        ssv = soup.find(href=re.compile("/help/vul#ssv")).string
        vulurl1 = vulurl + ssv[4:]
        myurl = "<a href='" + vulurl1 + "'>"+ssv+'</a>'
        print vulurl1
        titles.append(title)
        ssvs.append(myurl)
    print soup.find(href=re.compile("/help/vul#ssv")).string

            




 

if __name__ == '__main__':
    get_url()
    for url in  urls:
        code, head,data, errcode, _ = curl.curl2(url) 
        if code==200:
            get_title(data)









