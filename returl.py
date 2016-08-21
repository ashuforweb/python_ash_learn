# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
count = int(raw_input('Enter Count:'))
pos = int(raw_input('Enter Position:'))
cc = 1
def openURL(url,cc,p,co):
    print url
    cc = cc+1
    # print cc
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    # print tags[p-1]['href']
    if cc==co:
        print tags[p-1]['href']
        print tags[p-1].contents[0]
    else:
        openURL(tags[p-1]['href'],cc,p,co)
openURL(url,cc=0,p=pos,co=count)
