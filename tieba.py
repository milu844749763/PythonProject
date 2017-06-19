# -*- coding:utf-8 -*-
import urllib
import cookielib
import urllib2
import json
import re
from bs4 import BeautifulSoup
import time
import datetime
import requests
from random import choice

def rmpl(time,mid):
    url = "http://tieba.baidu.com/messagepool/listen"
    # 创建请求的request
    p = {"ie":"utf-8","ke":"美剧","fid":"582942","tid"}
    # 创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('sinacookie.txt', ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url)
    req.add_header("Referer", "http://weibo.com/1856927485/profile?topnav=1&wvr=6&is_all=1")
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36")
    req.add_header("X-Requested-With", "XMLHttpRequest")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req, urllib.urlencode(p))
    html = response.read().decode('gbk')
    print html