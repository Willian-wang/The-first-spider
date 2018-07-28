#-*- coding:utf-8 -*-
import urllib.request 
import http.cookiejar
from bs4 import BeautifulSoup
import txt_to_excel
import json
import time
import multiprocessing
import threading
import queue



class CatchDataThread(threading.Thread):
    #顾名思义，这玩意是用来抓取
    def __init__(self,threadID,Urlqueue,Dataqueue,lock):
        threading.Thread.__init__(self)
        self.Urlqueue=Urlqueue
        self.Dataqueue=Dataqueue
        self.threadID=threadID
        self.lock=lock
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    def run(self):
        print(str(self.threadID)+"号线程开始")
        global Counter_1
        global thread_EXIT
        global Counter_2
        while 1:
            lock.acquire()
            if self.Urlqueue.empty():
                lock.release()
                break
            num=self.Urlqueue.get()
            Counter_1=Counter_1+1
            print("+    "+str(Counter_1)+"/13176")
            lock.release()
            url="http://ce.sysu.edu.cn/hope/Diaries/Index_"+str(num)+".aspx"
            self.Dataqueue.put(RequireData(url,self.headers))
            lock.acquire()
            Counter_2=Counter_2+1
            print("-    "+str(Counter_2)+"/13176")
            ProduceData(self.Dataqueue.get())
            lock.release()
        print(str(self.threadID)+"号线程结束")

#class DealDataThread(threading.Thread):
#    def __init__(self,threadID,Dataqueue,lock,file):
#        threading.Thread.__init__(self)
#        self.Dataqueue=Dataqueue
#        self.Datalock=lock
#        self.file=file
#        self.threadID=threadID
#    def run(self):
#        global thread_EXIT
#        global Counter_2
#
#        print(str(self.threadID)+"号线程开始")
#        while 1:
#            lock.acquire()
#            if not self.Dataqueue.empty(): 
#                Counter_2=Counter_2+1
#                print("-    "+str(Counter_2)+"/13176")
#                ProduceData(self.Dataqueue.get())
#                lock.release()
#            else:
#                lock.release()
#                if not thread_EXIT:
#                    pass
#                else :
#                    break
#        print(str(self.threadID)+"号线程结束")
#                

def RequireData(url,headers):
    data=bytes(urllib.parse.urlencode({'用户名':'谢志强'},{'密码':''}),encoding='utf8')
    req=urllib.request.Request(url,headers=headers,method='GET')
    Response=urllib.request.urlopen(req)    
    TEXT=Response.read().decode('utf-8')
    return TEXT

def ProduceData(TEXT):
    soup=BeautifulSoup(TEXT,"lxml")
    content=soup.find_all("li",class_="internal_box_left_dairylist_li")
    for item in content:
        for string_item in item.stripped_strings:
            #print(string_item)
            file.write(string_item)
            file.write('\n')


thread_EXIT=0
Counter_1=0
Counter_2=0

file=open('日志.txt', 'w',encoding="utf-8") 
Urlqueue=queue.Queue(13176)
Dataqueue=queue.Queue()
threads=[]
lock=threading.Lock()

for i in range(1,301):
    Urlqueue.put(i)
for threadID in range(1,17):
    thread=CatchDataThread(threadID,Urlqueue,Dataqueue,lock)
    threads.append(thread)
    thread.start()
    time.sleep(0.4)


while not Urlqueue.empty ():
    pass

#for threadID in range(8,9):
#    thread=DealDataThread(threadID,Dataqueue,lock,file)
#    threads.append(thread)
#    thread.start()
#
while not Dataqueue.empty():
    pass

#time.sleep(15)

thread_EXIT+=1

for t in threads:
  t.join()

file.close()
txt_to_excel.txt_to_excel()
print("exit")




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
            #print(string_item)
            fileObject.write(string_item)
            fileObject.write('\n')
    print("Complete %s/13176"% n)


#n=0
#aue="http://ce.sysu.edu.cn/hope/Diaries/Index_0.aspx"
#fileObject = open('日志.txt', 'a',encoding="utf-8") 
#while n<13176:
#    str1=str(n)
#    str2=str(n+1)
#    aue=aue.replace(str1,str2)
#    getdata(aue,fileObject,n)
#    n=n+1
#fileObject.close()   
#txt_to_excel.txt_to_excel()