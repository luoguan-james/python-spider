#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:luoguan
# datetime:2019/9/4 14:15
# software: Pycharm 2019.1 python 3.5.4

import re
import urllib.request as ul
import urllib.error as ue
#彼岸网图片爬虫项目实战
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
opener = ul.build_opener()
opener.addheaders=[headers]  #请求浏览器的头,伪装成浏览器进行爬虫
ul.install_opener(opener)
for i in range(2,10):
    try:
        url = "http://pic.netbian.com/4kfengjing/index_"+str(i)+".html"
        data = ul.urlopen(url).read().decode("utf-8","ignore")
        pat = '<img src="(.*?)"'
        mydata = re.compile(pat).findall(data)
        for j in range(0,len(mydata)):
            mydata1 = "http://pic.netbian.com"+mydata[j]
            print(mydata1)
            file = "E://爬虫图片/"+str(i)+str(j)+".jpg"
            ul.urlretrieve(mydata1,file)
            print("第%d %d次成功"%(i,j))
    except ue.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
            time.sleep(10)
    except Exception as e:
        print("Exception:" + str(e))
        time.sleep(1)