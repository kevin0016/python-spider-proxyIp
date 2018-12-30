# coding:utf-8
import urllib
import time
import socket
import random
import json

from ipchi import Proxy_ip, UserAgent, Mysql_Config

res_list = []


def Visitpage(proxyip, url):
    """
       通过代理IPget请求某个页面
       :param proxyip: 代理IP
       :param url:  访问URL
       :return:
    """
    socket.setdefaulttimeout(6)
    proxy_support = urllib.ProxyHandler({'http': proxyip})
    user_agent = random.choice(UserAgent.user_agents)
    opener = urllib.build_opener(proxy_support, urllib.HTTPHandler)
    urllib.install_opener(opener)
    try:
        request = urllib.Request(url)
        request.add_header('Referer', 'http://www.baidu.com')
        request.add_header('User-Agent', user_agent)
        request.add_header('Content-type', 'application/json;charset=UTF-8')
        reponse = urllib.urlopen(request).read()
        # print(reponse)
        json_format = check_json_format(reponse)
        if (json_format):
            print(reponse)
            return reponse
        time.sleep(random.randint(10, 20))
    except urllib.URLError as e:
        print('URLError! The bad proxy is %s' % proxyip)
    except urllib.HTTPError as e:
        print('HTTPError! The bad proxy is %s' % proxyip)
    except:
        print('Unknown Errors! The bad proxy is %s ' % proxyip)


def Clicklikebutton(proxyip, url, data):
    socket.setdefaulttimeout(6)
    proxy_support = urllib.ProxyHandler({'http': proxyip})
    user_agent = random.choice(UserAgent.user_agents)
    opener = urllib.build_opener(proxy_support, urllib.HTTPHandler)
    try:
        request = urllib.Request(url)
        request.add_header('Referer', 'http://www.baidu.com')
        request.add_header('User-Agent', user_agent)
        request.add_header('Content-type', 'application/json;charset=UTF-8')
        data = urllib.urlencode(data)
        resp = opener.open(request, data)
        print(resp.read())
        time.sleep(random.randint(60, 180))
    except urllib.URLError as e:
        print('URLError! The bad proxy is %s' % proxyip)
    except urllib.HTTPError as e:
        print('HTTPError! The bad proxy is %s' % proxyip)
    except:
        print('Unknown Errors! The bad proxy is %s ' % proxyip)


def check_json_format(raw_msg):
    """
    用于判断一个字符串是否符合Json格式
    :param self:
    :return:
    """
    if isinstance(raw_msg, str):  # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False


def getData(lat, lon):
    visitpagelist = []
    for i in range(len(Proxy_ip.iplist)):
        proxyip = Proxy_ip.iplist[i]
        i += 1
        print(proxyip)
        for m in range(random.randint(2, 4)):
            url = 'http://api.cellocation.com:81/rewifi/?lat=' + lat + '&lon=' + lon + '&n=10'
            print(url)
            visitpage = Visitpage(proxyip, url)
            if visitpage is not None:
                visitpagelist.append(visitpage)
        if len(visitpagelist):
            return visitpagelist


def main():
    get_count_sh_area = Mysql_Config.getCountShArea()
    limitPage = 10
    for index in range(0, get_count_sh_area):
        areas = Mysql_Config.getShArea(index, limitPage)
        index = index + limitPage
        print(areas)
        for area in areas:
            print(area)
            lat = area['lat']
            lng = area['lng']
            data = getData(lat, lng)
            print(data)


if __name__ == "__main__":
    main()
