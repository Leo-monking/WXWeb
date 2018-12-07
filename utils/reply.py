# -*- coding: utf-8 -*-
'''
    Created on 2017-8-20
    filename: reply.py
    @author: MONKING
    
    内容描述：
    消息回复，消息类型主要包括text、image
'''

import time,requests


def GetResponseByTuLing(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    TULING_KEY = '04f44290d4cf462aae8ac563ea7aac16'
    data = {
        'key'    : TULING_KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        msg = r.get('text')
        return msg.encode("utf-8")
    except:
        return "tuling has error"

class Msg(object):
    def __init__(self):
        pass
    def send(self):
        return "Success"

class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = GetResponseByTuLing(content)

    def send(self):
        XmlForm = '''
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        '''
        return XmlForm.format(**self.__dict)
class ImageMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId
    def send(self):
        XmlForm = '''
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        '''
        return XmlForm.format(**self.__dict)

class LocationMsg(Msg):
    def __init__(self, toUserName, fromUserName, locationX, locationY, scale, label):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Location_X'] = locationX
        self.__dict['Location_Y'] = locationY
        self.__dict['Scale'] = scale
        self.__dict['Label'] = label
    def send(self):
        XmlForm = '''
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[location]]></MsgType>
		<Location_X>{locationX}</Location_X>
		<Location_Y>{locationY}</Location_Y>
		<Scale>{Scale}</Scale>
		<Label><![CDATA[{label}]]></Label>
        </xml>
        '''
        return XmlForm.format(**self.__dict)
        
class VoiceMsg(Msg):
    def __init__(self, toUserName, fromUserName, mediaId, format):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['MediaId'] = mediaId
        self.__dict['Format'] = format
    def send(self):
        XmlForm = '''
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[voice]]></MsgType>
        <Voice>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        <Format><![CDATA[{Format}]]></Format>
        </Voice>
        </xml>
        '''
        return XmlForm.format(**self.__dict)
