import requests
from bs4 import BeautifulSoup
url = raw_input("Please enter the url")
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
nums = soup.findAll("span",{"class":"comments"})
sums = []
print len(nums)
for i in range(0,len(nums)):
    # print int(nums[i].getText())
    sums.append(int(nums[i].getText()))
print sum(sums)
