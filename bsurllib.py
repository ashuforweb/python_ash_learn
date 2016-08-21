# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sums=[]
print len(tags)
for tag in tags:
    sums.append(int(tag.contents[0]))
print sum(sums)
