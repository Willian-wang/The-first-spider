import urllib.request 
import http.cookiejar
from bs4 import BeautifulSoup

#cookie=http.cookiejar.CookieJar()
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#headers=urllib.request.HTTPCookieProcessor(cookiejar=cookie)
#dict = {'name':'Germey'}
data=bytes(urllib.parse.urlencode({'用户名':'谢志强'},{'密码':''}),encoding='utf8')
req=urllib.request.Request("http://ce.sysu.edu.cn/hope/html/Internal/Journals/index.html",data=data,headers=headers,method='GET')
Response=urllib.request.urlopen(req)

TEXT=Response.read().decode('utf-8')
soup=BeautifulSoup(TEXT,"lxml")
#print(soup)
content=soup.find_all("li",class_="internal_box_left_dairylist_li")
#print(content)
for item in content:
    for string_item in item.stripped_strings:
        print(string_item)