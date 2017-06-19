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

my = ["长夏已尽，凛冬将至。 -----------------天堂美剧观光团  看最新最热美剧 来天堂美剧. www.tiantangmeiju.com   ",
      "世界上到处都是不太可能的友谊。它们都是由一方迫切的需求和另一方伸出的援助之手开始的。 -----------------天堂美剧观光团  看最新最热美剧 来天堂美剧      www.tiantangmeiju.com  ",
      "家人，这世上最珍贵的风景。困难时他们突然出现；有意无意时他们助推成功；守秘时他们相依为伴-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧      www.tiantangmeiju.com      ",
      "在权力的游戏之中，你不当赢家，就只有死路一条，没有中间地带。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧   www.tiantangmeiju.com",
      "我们有能力去爱，那是对我们最美好的恩赐，却也是我们最深沉的悲哀。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧  www.tiantangmeiju.com",
      "最愚蠢的人通常也比嘲笑他们的家伙聪明.-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧       www.tiantangmeiju.com",
      "死的历史用墨水书写，活的历史则用鲜血。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧     www.tiantangmeiju.com ",
      "虽然全天下的侏儒都可能被视为私生子，私生子却不见得要被人视为侏儒。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧  www.tiantangmeiju.com",
      "我们生来便是为了受苦，而受苦会让我们坚强。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧    www.tiantangmeiju.com ",
      "眼泪并不是女人惟一的武器，你两腿之间还有一件，最好学会用它。一旦学成，自有男人主动为你使剑。两种剑都免费。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧    www.tiantangmeiju.com  ",
      "勇气和愚蠢往往只有一线之隔。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧    www.tiantangmeiju.com    ",
      "长夜将至，我从今开始守望，至死方休。我将不娶妻，不封地，不生子。我将不戴宝冠，不争荣宠。我将尽忠职守，生死于斯。我是黑暗中的利剑，长城上的守卫，抵御寒冷的烈焰，破晓时分的光线，唤醒眠者的号角，守护王国的坚盾。我将生命与荣耀献给守夜人，今夜如此，夜夜皆然。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧   www.tiantangmeiju.com  ",
      "戴上王冠的狗，在拴起来就难了。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧       www点tiantangmeiju点com",
      "我云游四海，见过不同的民族，说不同的语言信仰不同的神，在我看来，唯一的真神就在女人的两腿之间。-----------------天堂美剧观光团  看最新最热美剧 来天堂美剧    www.tiantangmeiju.com   "
      ]

def test():
    url = "http://weibo.com/u/1856927485/home?leftnav=1"
    print url
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
    response = opener.open(req)
    html = response.read().decode('utf-8')
    print html

def remark2(time):
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('sinacookie.txt', ignore_discard=True, ignore_expires=True)
    session = requests.Session()
    url = "http://weibo.com/aj/v6/comment/add?ajwvr=6&__rnd=" + time
    print  url
    login_data = {'act': 'post', 'mid': "4097972839026091",'uid': "1856927485", 'forward': 0,
            'isroot': 0, 'content': "stest0000", 'location': 'page_100505_home', 'module': "scommlist",
            "group_source":"","pdetail":"1005051856927485","_t":0}
    headers2 = {'Cookie': "SINAGLOBAL=5331080382798.126.1490625872713; UM_distinctid=15b1f817e771f6-05c3b5c933d018-396b4c0b-144000-15b1f817e78186; un=844749763@qq.com; wvr=6; YF-Ugrow-G0=5b31332af1361e117ff29bb32e4d8439; SCF=AhEKgxDXrTI4BBLd6Q30ucG5nNTXwafxOrhgjmTcCjrvar1JT0jtXsppEv037WkuHkIkQWOUXeMinqItDEB7Qno.; SUB=_2A2518bIKDeThGedG7lQY8inIwzmIHXVWhqTCrDV8PUNbmtBeLVOikW8avWRdvAw3kxHOANL_ykh9-kB5nA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh2sShBGOyI3W5GA3dJXwCi5JpX5KzhUgL.Fo2RSKq4eoMX1h-2dJLoIEHki--ci-zRi-24i--ciKLsiK.Xi--RiKn7iKyhi--Xi-iFi-2f; SUHB=04W_S08JA4hE13; ALF=1524037082; SSOLoginState=1492501082; YF-V5-G0=c2f54dafbe53b1d2f7183e51668d457a; _s_tentry=login.sina.com.cn; Apache=6129169067090.48.1492501083755; ULV=1492501083844:12:10:7:6129169067090.48.1492501083755:1492491396570; YF-Page-G0=8fee13afa53da91ff99fc89cc7829b07; wb_publish_fist100_1856927485=1; UOR=,,www.baidu.com",
               "Referer":"http://weibo.com/1856927485/profile?topnav=1&wvr=6&is_all=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36",
               "X-Requested-With":"XMLHttpRequest"
               }
    r = session.post(url, data=login_data,headers=headers2)
    res_value = r.json()
    print  res_value


def jx(time):
    url = "http://weibo.com/aj/v6/comment/add?ajwvr=6&__rnd=" + time
    print url
    # 创建请求的request
    p = {'act': 'post', 'mid': "4097972839026091",'uid': "1856927485", 'forward': 0,
            'isroot': 0, 'content': "dkjsakdjkadjka", 'location': 'page_100505_home', 'module': "scommlist",
            "group_source":"","pdetail":"1005051856927485","_t":0}
    # 创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('sinacookie.txt', ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url)
    req.add_header("Referer","http://weibo.com/1856927485/profile?topnav=1&wvr=6&is_all=1")
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36")
    req.add_header("X-Requested-With","XMLHttpRequest")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req, urllib.urlencode(p))
    html = response.read().decode('gbk')
    print html


def rmpl(time,mid):
    url = "http://d.weibo.com/aj/v6/comment/add?ajwvr=6&__rnd=" + time
    # 创建请求的request
    p = {'act': 'post', 'mid': mid, 'uid': "2391667284", 'forward': 0,
         'isroot': 0, 'content': choice(my), 'location': 'page_102803_ctg1_1760_-_ctg1_1760_home', 'module': "scommlist",
         "group_source": "", "pdetail": "102803_ctg1_1760_-_ctg1_1760", "_t": 0}
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





def get(time):
    url = "http://d.weibo.com/p/aj/v6/mblog/mbloglist"
    p={
        "ajwvr":"6",
        "domain": "102803_ctg1_1760_-_ctg1_1760",
        "topnav": "1",
        "mod": "logo",
        "wvr": "6",
        "pagebar": "0",
        "tab": "home",
        "current_page": "1",
        "pre_page": "1",
        "page": "1",
        "pl_name": "Pl_Core_NewMixFeed__3",
        "id": "102803_ctg1_1760_-_ctg1_1760",
        "script_uri": "/",
        "feed_type":"1",
        "domain_op": "102803_ctg1_1760_-_ctg1_1760",
        "__rnd":time
    }
    # 创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('sinacookie.txt', ignore_discard=True, ignore_expires=True)
    req = urllib2.Request("%s?%s" %(url, urllib.urlencode(p)))
    req.add_header("Referer", "http://weibo.com/1856927485/profile?topnav=1&wvr=6&is_all=1")
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36")
    req.add_header("X-Requested-With", "XMLHttpRequest")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req,urllib.urlencode(p))
    html = response.read().decode('utf-8')
    ddata = json.loads(html)
    str = ddata["data"]
    soup = BeautifulSoup(str)
    table_soup = soup.select('.WB_cardwrap.WB_feed_type.S_bg2.WB_feed_vipcover')
    if len(table_soup):
        print table_soup[0].get("mid")
        rmpl(zhengchang, table_soup[0].get("mid"))
    else:
        print "no crawl"


def www(time):
    url="http://d.weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=102803_ctg1_1760_-_ctg1_1760&topnav=1&mod=logo&wvr=6&pagebar=0&tab=home&current_page=1&pre_page=1&page=1&pl_name=Pl_Core_NewMixFeed__3&id=102803_ctg1_1760_-_ctg1_1760&script_uri=/&feed_type=1&domain_op=102803_ctg1_1760_-_ctg1_1760&__rnd=1492586091612"
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
    response = opener.open(req)
    html = response.read().decode('utf-8')
    ddata = json.loads(html)
    str = ddata["data"]
    pl = '<a href="(.*)">(.*)</a>'
    pll= '<div>'
    matcher1 = re.findall(pll,str)
    print matcher1




for i in range(1,60):
    shu = time.time() * 1000
    zhengchang = "%.f" % float(shu)
    print zhengchang
    get(zhengchang)
    time.sleep(121)

