﻿# -*- coding: utf-8 -*-
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
			#appId = "wx5f490cedc2deb9e6"
			#appSecret = "c5988955612e8303770788b4da00a997"
			appId = "wxc42cdded0a80792a"
			appSecret = "802c6edba56dfa685f05cadb2228230a"
		postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))
		print "access_token get:",postUrl
		urlResp = urllib.urlopen(postUrl)
		rspRet = urlResp.read()
		print "get access_token ret:",rspRet
		urlResp = json.loads(rspRet)
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