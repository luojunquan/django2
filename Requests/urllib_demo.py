#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib


URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'
def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    print '>>>>>>Response Headders'
    print response.info()
    print '>>>>>>Response Body'
    print ''.join([line for line in response.readlines()])


def use_parms_urllib2():
    parms = urllib.urlencode({'param1':'hello','param2':'world'})
    print 'Request Params'
    print parms
    response = urllib.urlopen('?'.join([URL_GET,'%s']) % parms)
    print '>>>>>>Status Code'
    print response.getcode()
    print '>>>>>>Response Body'
    print ''.join([line for line in response.readlines()])



if __name__ == '__main__':
    print '>>>Use simple urllib2'
    use_simple_urllib2()
    # print '>>>Use Params urllib2'
    # use_parms_urllib2()