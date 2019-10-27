#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:luoguan
# datetime:2019/9/5 15:49
# software: Pycharm 2019.1 python 3.5.4
import re
import urllib.request as ul
import urllib.error as ue
#彼岸网图片爬虫项目实战
headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36")
opener = ul.build_opener()
opener.addheaders=[headers]  #请求浏览器的头,伪装成浏览器进行爬虫
ul.install_opener(opener)
while True:
    try:
        keyword = input("请输入学号：")
        keyword = ul.quote(keyword)
        url = "http://bkjwgl.nefu.edu.cn/dblydx//uploadfile/studentphoto/pic/"+keyword+".JPG"
        data = ul.urlopen(url).read().decode("utf-8","ignore")
        file = "E:/教务系统爬虫/"+keyword+".jpg"
        ul.urlretrieve(url,file)
        print("爬取成功")
    except ue.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
            time.sleep(10)
    except Exception as e:
        print("Exception:" + str(e))
        time.sleep(1)