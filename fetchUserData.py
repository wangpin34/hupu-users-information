# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import urllib2
import sys

print sys.getdefaultencoding()

reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'

print sys.getdefaultencoding()

proxy=urllib2.ProxyHandler({'http': 'web-proxy.austin.hp.com:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)



def funcA():
    print 'This is funcA'

def funcB():
    print 'This is funcB'

def fetchDoc(url):
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError, e:
        print e.reason
        return
    return response.read()

def genProfile(fields):
    length = len(fields)
    n = 0
    profile = {}
    while n < length:
        key = fields[n]
        value = fields[n + 1]
        profile[key] = value
        n = n + 2
    return profile


def parseProfile(html):
    doc = pq(html)
    print 'parsing...'
    content = doc('#content')

    name =  content.find('h1').text()

    fields = []
    for dom in content.find('table td'):
        fields.append(dom.text)

    profile = genProfile(fields)

    print name
    for key in profile:
        print '%s - %s'%(key, profile[key])
