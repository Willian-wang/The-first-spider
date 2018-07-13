#-*- coding:utf-8 -*-
import urllib.request 
import http.cookiejar
from bs4 import BeautifulSoup

def getdata(aue,fileObject,n):
    #cookie=http.cookiejar.CookieJar()
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    #headers=urllib.request.HTTPCookieProcessor(cookiejar=cookie)
    #dict = {'name':'Germey'}
    data=bytes(urllib.parse.urlencode({'用户名':'谢志强'},{'密码':''}),encoding='utf8')
    req=urllib.request.Request(aue,data=data,headers=headers,method='GET')
    Response=urllib.request.urlopen(req)
    
    TEXT=Response.read().decode('utf-8')
    soup=BeautifulSoup(TEXT,"lxml")
    #print(soup)
    content=soup.find_all("li",class_="internal_box_left_dairylist_li")
    #print(content)
    n=str(n)
    for item in content:
        for string_item in item.stripped_strings:
            print(string_item)
            fileObject.write(string_item)
            fileObject.write('\n')
    #aue=soup.find("a",string=n)
    #aue=aue['href']
    #return aue

n=0
aue="http://ce.sysu.edu.cn/hope/html/Internal/Journals/index_0.html"
fileObject = open('日志.txt', 'a',encoding="utf-8")  
while n<350:
    str1=str(n)
    str2=str(n+1)
    aue=aue.replace(str1,str2)
    getdata(aue,fileObject,n)
    n=n+1
fileObject.close()  