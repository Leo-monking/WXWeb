# -*- coding: utf-8 -*-
'''
    Created on 2017-8-20
    filename: receive.py
    @author: MONKING
    
    内容描述：
    消息分类，分析关键参数
'''

import xml.etree.ElementTree as ET

TULING_KEY = '04f44290d4cf462aae8ac563ea7aac16'
def GetResponseByTuLing(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : TULING_KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

def parse_xml(web_data):
	if len(web_data) == 0:
		return None
	root = ET.fromstring(web_data)
	msg_type = root.find('MsgType').text
	if msg_type == 'text':
		return TextMsg(root)
	if msg_type == 'image':
		return ImageMsg(root)
	if msg_type == 'voice':
		return VoiceMsg(root)
	if msg_type == 'location':
		return LocationMsg(root)

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
		self.Content = GetResponseByTuLing(xmlData.find('Content').text.encode("utf-8"))

class ImageMsg(Msg):
	def __init__(self, xmlData):
		Msg.__init__(self, xmlData)
		self.PicUrl = xmlData.find('PicUrl').text
		self.MediaId = xmlData.find('MediaId').text
		
class VoiceMsg(Msg):
	def __init__(self, xmlData):
		Msg.__init__(self, xmlData)
		self.MediaId = xmlData.find('MediaId').text
		self.Format = xmlData.find('Format').text

class LocationMsg(Msg):
	def __init__(self, xmlData):
		Msg.__init__(self, xmlData)
		self.Location_X = xmlData.find('Location_X')
		self.Location_Y = xmlData.find('Location_Y')
		self.Scale = xmlData.find('Scale')
		self.Label = xmlData.find('Label').text
