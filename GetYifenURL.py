#!/usr/bin/python 
import urllib2
import cookielib
#import Cookie
def makeCookie(name, value):
    return cookielib.Cookie(version=0, 
        name=name, 
        value=value,
        port=None, 
        port_specified=False,
        domain="www.yifen.com", 
        domain_specified=True, 
        domain_initial_dot=False,
        path="/", 
        path_specified=True,
        secure=False,
        expires=None,
        discard=False,
        comment=None,
        comment_url=None,
        rest=None)

def GetYifenURL():
	req = urllib2.Request(url='http://www.yifen.com/member/logon')
	req.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			 'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
			 'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
	}

	cj = cookielib.CookieJar()
	#cj.set_cookie(makeCookie("amvid", "0e58dcd7a29d62a14ed13310ccd5b273"))
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	urllib2.install_opener(opener)
	
	r = opener.open(req)
	
	#print cj
	
	req2 = urllib2.Request(url='http://www.yifen.com/ImgCode.aspx')
	req2.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			 'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
			 'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
	}
	r = opener.open(req2)
	
	#print cj
	
	req3 = urllib2.Request(url='http://www.yifen.com/member/logonPost')
	req3.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			 'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
			 'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
	}
	req3.data = 'name=weple%40qq.com&pass=zwp001&checkCode=&isCode=1&autoLogon=1'
	r = opener.open(req3)
	#print cj
	
	req4 = urllib2.Request(url='http://www.yifen.com/home/dosignin')
	req4.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			 'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
			 'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
	}
	
	r = opener.open(req4, "")
	return r.read()
