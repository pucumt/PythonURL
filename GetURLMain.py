#coding=utf-8
#!/usr/bin/python

import thread
#import threading
import time
import GetManmanbuyURL
import GetYifenURL
import Get51biURL
        
def GetURLMain(): # the detail functions
	try:
		GetManmanbuyURL.GetManmanbuyURL()
	except:
		print "Manmanbuy error!"

	try:
		GetYifenURL.GetYifenURL()
	except:
		print "Yifen error!"

	#try:
	#	print Get51biURL.Get51biURL()
	#except:
	#	print "51bi error!"

	print "Hello world!"

if __name__ == '__main__':
	GetURLMain()

#86400 = 24 hour