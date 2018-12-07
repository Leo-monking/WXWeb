# -*- coding: utf-8 -*-
'''
    Created on 2017-8-20
    filename: basic.py
    @author: MONKING
    
    内容描述：
    通过该接口获取access_token
'''
import urllib
import time
import json

class Basic():
	def __init__(self):
		print "__init__(self)"
		self.__accessToken = ''
		self.__leftTime = 0
	def __real_get_access_token(self,appId,appSecret):
		if (appId == "") or (appSecret ==""):
			appId = "wxb33c022be92586ff"
			appSecret = "e2f40f2973751bb2223078815224aead"
		postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))
		urlResp = urllib.urlopen(postUrl)
		urlResp = json.loads(urlResp.read())
		if "access_token" in urlResp.keys():
			self.__accessToken = urlResp['access_token']
			self.__leftTime = urlResp['expires_in']
		else:
			self.__accessToken = ""
			self.__leftTime = 0
		
	def get_access_token(self,appId,appSecret):
		if self.__leftTime < 10:
			self.__real_get_access_token(appId,appSecret)
		return self.__accessToken
		
	def run(self):
		while(True):
			if self.__leftTime > 10:
				time.sleep(2)
				self.__leftTime -= 2
			else:
				self.__real_get_access_token()
