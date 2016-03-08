__author__ = 'zdz8207'
from bs4 import BeautifulSoup

import urllib.request
import urllib.parse
import re
import urllib.request, urllib.parse, http.cookiejar

def getHtml(url):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
                         ('Cookie', '4564564564564564565646540')]

    urllib.request.install_opener(opener)

    html_bytes = urllib.request.urlopen(url).read()
    html_string = html_bytes.decode('utf-8')
    return html_string

html_doc = getHtml("http://zst.aicai.com/ssq/openInfo/")
soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.title)
#table = soup.find_all('table', class_='fzTab')
#print(table)#<tr onmouseout="this.style.background=''" 这种tr丢失了

tr = soup.find('tr',attrs={"onmouseout": "this.style.background=''"})
#print(tr)
tds = tr.find_all('td')
opennum = tds[0].get_text()
#print(opennum)

reds = []
for i in  range(2,8):
    reds.append(tds[i].get_text())
#print(reds)
blue = tds[8].get_text()
#print(blue)

#把list转换为字符串:(',').join(list)
#最终输出结果格式如：2015075期开奖号码：6,11,13,19,21,32, 蓝球：4
print(opennum+'期开奖号码：'+ (',').join(reds)+", 蓝球："+blue)
