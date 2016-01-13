#!/usr/bin/python 
import urllib2
import cookielib
import time
from HTMLParser import HTMLParser 
from sgmllib import SGMLParser
import httplib

class MyParser(SGMLParser):  
    elementID = ""
    url = ""
    pages = ""
      
    def finish_starttag(self, tag, attrs):
        SGMLParser.finish_starttag(self, tag, attrs)
        if tag == 'a':  
            if ('id', self.elementID) in attrs:
                self.url = attrs[4][1] 
        if tag == 'input':
            if('id', 'page') in attrs:
                self.pages = attrs[3][1]


class ChunkParser(HTMLParser):  
    url = ""

    def handle_starttag(self,tag,attr):  
        if tag == 'meta' and ('http-equiv', 'refresh') in attr:  
            self.url = attr[1][1][6:]

def Get51biURL():
    t = time.gmtime()

    req = urllib2.Request(url='http://www.51bi.com/loginForAjax.html ')
    req.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	   	   'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		   'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
    }
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    req.data = 'loginname=weple%40qq.com&md5password=6C243D508B6A399E0E1606E1A1E42A36&currentUrl=http%3A%2F%2Fwww.51bi.com%2F&cookieflag=yes'
    urllib2.install_opener(opener)
    print 'step 1 ...'
    r = opener.open(req)

    req2 = urllib2.Request(url='http://www.51bi.com/bbs/viewThread.jhtml?year={0}&month={1}&day={2}'.format(t.tm_year,t.tm_mon,t.tm_mday))
    req2.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
    }
    print 'step 2 ...'
    r = opener.open(req2)

    urlSign = r.url
    urlID = urlSign[31:40]

    myparser = MyParser()
    myparser.elementID = "buy_url_{0}".format(urlID)
    strRead = r.read()
    myparser.feed(strRead)
    myparser.close()
    
    page = myparser.pages

    req3 = urllib2.Request(url=myparser.url)
    req3.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
    }
    print 'step 3 ...'
    r = opener.open(req3)

    #id=286367839
    # /zhekou/zhekou/checkQDKey.jhtml /zhekou/zhekou/checkQDKey.jhtm
    #'http://www.51bi.com/tracert.html?link=http%3A%2F%2Fwww.51bi.com%2Fgoshopping.jhtml%3Flink%3Dhttp%253A%252F%252Fwww.tootoo.cn%252Fsale%252Fsh%252F15%252Fsahuan%252F%26fromPage%3Dtuotuogongshe%26tracert%3D1+&fromPage=zhekouqiandao&adcontentid=8964&adposid=231&tracert=1'
    #                                                                 '/goshopping.jhtml?link=http%3A%2F%2Fwww.tootoo.cn%2Fsale%2Fsh%2F15%2Fsahuan%2F&fromPage=tuotuogongshe&tracert=1'
    myparser = ChunkParser()
    myparser.feed(r.read())

    req4 = urllib2.Request(url=myparser.url)
    req4.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
    }
    print 'step 4 ...'
    r = opener.open(req4)

    req5 = urllib2.Request(url='http://www.51bi.com/zhekou/zhekou/checkQDKey.jhtml')
    req5.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
    }
    req5.data = 'id={0}'.format(urlID)
    print 'step 5 ...'
    r = opener.open(req5)

    cj.clear(domain='.51bi.com', path='/', name='bibi_adcontentid_go')
    cj.clear(domain='.51bi.com', path='/', name='bibi_adfrompage_go')
    cj.clear(domain='.51bi.com', path='/', name='tracert_adcontid51bi')
    cj.clear(domain='.51bi.com', path='/', name='tracert_adposid51bi')


	# Register the streaming http handlers with urllib2
#register_openers()

# Start the multipart/form-data encoding of the file "DSC0001.jpg"
# "image1" is the name of the parameter, which is normally set
# via the "name" parameter of the HTML <input> tag.

# headers contains the necessary Content-Type and Content-Length
# datagen is a generator object that yields the encoded parameters
#datagen, headers = multipart_encode({"image1": open("DSC0001.jpg")})

# Create the Request object
#request = urllib2.Request("http://localhost:5000/upload_image", datagen,
#headers)

   # errcode, errmsg, headers = h.getreply()
   # return h.file.read()


   
    body = '''------WebKitFormBoundaryNfDZ8ywDmf5pEXDA
Content-Disposition: form-data; name="id"

{0}
------WebKitFormBoundaryNfDZ8ywDmf5pEXDA
Content-Disposition: form-data; name="type"

sa
------WebKitFormBoundaryNfDZ8ywDmf5pEXDA
Content-Disposition: form-data; name="flagHits"

1
------WebKitFormBoundaryNfDZ8ywDmf5pEXDA
Content-Disposition: form-data; name="blqdtype"

1
------WebKitFormBoundaryNfDZ8ywDmf5pEXDA
Content-Disposition: form-data; name="page"

{1}
------WebKitFormBoundaryNfDZ8ywDmf5pEXDA
Content-Disposition: form-data; name="content"

1111111111111111111111111111
------WebKitFormBoundaryNfDZ8ywDmf5pEXDA--
'''.format(urlID, page)

    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	            'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
                'Proxy-Connection':'keep-alive',
                'Origin':'http://www.51bi.com',
                'Referer':urlSign,
                'Cache-Control': 'max-age=0',
                'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryNfDZ8ywDmf5pEXDA'
    }
    h = httplib.HTTPConnection('www.51bi.com')
    h.request('POST', '/bbs/replyBiThread.html?', body, headers)
    r = h.getresponse()

    #req6.headers =
    #{'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #            'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	   #         'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
    #            'Proxy-Connection':'keep-alive',
    #            'Origin':'http://www.51bi.com',
    #            'Referer':urlSign,
    #            'Cache-Control': 'max-age=0',
    #            'Content-Type': 'multipart/form-data;
    #            boundary=----WebKitFormBoundaryNfDZ8ywDmf5pEXDA'
    #}
    print 'step 6 ...'
    return r
    #r = opener.open(req6)
    #return r.read()

 #   print cj
 #  print r.info() 



