# -*- coding: utf-8 -*-
'''
    Created on 2017-8-20
    filename: receive.py
    @author: MONKING
    
    内容描述：
    消息分类，分析关键参数
'''

import xml.etree.ElementTree as ET

def parse_xml(web_data):
	if len(web_data) == 0:
		return None
	root = ET.fromstring(web_data)
	msg_type = root.find('MsgType').text
	if msg_type == 'text':
		return TextMsg(root)
	elif msg_type == 'image':
		return ImageMsg(root)

class Msg(object):
	def __init__(self, xmlData):
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		self.MsgId = xmlData.find('MsgId').text

class TextMsg(Msg):
	def __init__(self, xmlData):
		Msg.__init__(self, xmlData)
		self.Content = xmlData.find('Content').text.encode("utf-8")

class ImageMsg(Msg):
	def __init__(self, xmlData):
		Msg.__init__(self, xmlData)
		self.PicUrl = xmlData.find('PicUrl').text
		self.MediaId = xmlData.find('MediaId').text
