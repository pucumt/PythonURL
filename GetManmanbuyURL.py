#coding=utf-8
#!/usr/bin/python

import urllib2
import cookielib

def GetManmanbuyURL():
    req = urllib2.Request(url='http://home.manmanbuy.com/login.aspx?tourl=http%3a%2f%2fwww.manmanbuy.com%2fdefault.aspx')
    req.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		 'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		 'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
	}
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    r = opener.open(req)
    
    req.data = '__VIEWSTATE=%2FwEPDwUKMTUyNjkyMjAxMGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFCWF1dG9Mb2dpbmCv5H6%2B4LetVKUd9rdD4sHPc%2FQc&__EVENTVALIDATION=%2FwEWBQKguLKzCQLB2tiHDgLKw6LdBQKWuuO2AgKC3IeGDDBVb6R%2BhUSGlBJMK5KTonnxrT2j&txtUser=pucumt&txtPass=zwp001&autoLogin=on&btnLogin=%B5%C7%C2%BD'
                
    r = opener.open(req)
    
    req2 = urllib2.Request(url='http://www.manmanbuy.com/chart.aspx?DA={0}+0800%20(China%20Standard%20Time)')
    req2.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		 'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		 'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
	}
    req2.data = 'action=daka&u=pucumt'
    r = opener.open(req2)
    
    return r
    
