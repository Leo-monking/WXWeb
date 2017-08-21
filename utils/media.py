# -*- coding: utf-8 -*-
'''
    Created on 2017-8-20
    filename: media.py
    @author: MONKING
    
    内容描述：
    上传图片素材
'''
from basic import Basic
import urllib2
import poster.encode
from poster.streaminghttp import register_openers

class Media(object):
    def __init__(self):
        register_openers()
    #上传图片
    def uplaod(self, access_Token, filePath, mediaType):
        openFile = open(filePath, "rb")
        param = {'media': openFile}
        postData, postHeaders = poster.encode.multipart_encode(param)

        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (access_Token, mediaType)
        request = urllib2.Request(postUrl, postData, postHeaders)
        urlResp = urllib2.urlopen(request)
        print urlResp.read()

if __name__ == '__main__':
    myMedia = Media()
    access_Token = Basic().get_access_token()
    if access_Token != "":
    	filePath = "D:/wxmp/baby.jpg"   #请安实际填写
    	mediaType = "image"
    	myMedia.uplaod(access_Token, filePath, mediaType)
    else:
		print u"access_Token 获取失败，无法正常上传素材！"