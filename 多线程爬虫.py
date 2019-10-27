#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:luoguan
# datetime:2019/9/4 16:38
# software: Pycharm 2019.1 python 3.5.4
import re
import urllib.request as ul
import urllib.error as ue
import threading
import time
#多线程同时进行工作，提高工作效率
class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,10):
            print("大家好")
class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,10):
            print("我是渣渣辉")
a = A()
a.start()
b = B()
b.start()



