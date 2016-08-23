import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
caseFile = open("/ashudev/icert/caseFile2.csv","w")
for i in range(378,551):
    r = requests.get('http://www.trackitt.com/usa-immigration-trackers/i140/page/'+str(i))
    soup = BeautifulSoup(r.content,"html.parser")
    table = soup.find("table",{"class":"fancyTable"})
    print 'running'+str(i)
    for tr in table.find_all('tr')[2:]:
        tds = tr.find_all('td')
        country = tds[4].getText()
        applicantType = tds[5].getText()
        serviceCenter = tds[6].getText()
        category = tds[7].getText()
        priorityDate = tds[8].getText()
        applicationFiled = tds[9].getText()
        recDate = tds[10].getText()
        noticeDate = tds[11].getText()
        processingType = tds[14].getText()
        rfe = tds[15].getText()
        rfeDate = tds[16].getText()
        reasonrfe = tds[17].getText()
        rfeRepiedDate = tds[18].getText()
        appStatus = tds[19].getText()
        appDate = tds[20].getText()
        caseFile.write(country+';'+applicantType+';'+serviceCenter+';'+category+';'+priorityDate+';'+applicationFiled+';'+recDate+';'+noticeDate+';'+processingType+';'+rfe+';'+rfeDate+';'+reasonrfe+';'+rfeRepiedDate+';'+appStatus+';'+appDate)

caseFile.close()
