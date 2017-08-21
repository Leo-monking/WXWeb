# -*- coding: utf-8 -*-
'''
    Created on 2017-8-20
    filename: menu.py
    @author: MONKING
    
    内容描述：
    菜单相关操作，以及示例
'''

import urllib
from basic import Basic
menuJson = '''
    {
        "button":
        [
            {
                "type": "click",
                "name": "开发指引",
                "key":  "mpGuide"
            },
            {
                "name": "公众平台",
                "sub_button":
                [
                    {
                    	"type": "click",
                    	"name": "开发指引",
                    	"key":  "mpGuide01"
                    },
                    {
                    	"type": "click",
                    	"name": "聊斋",
                    	"key":  "mpGuide02"
                    },
                    {
                    	"type": "click",
                    	"name": "妖怪",
                    	"key":  "mpGuide03"
                    }
                ]
            },
            {
                "type": "click",
                "name": "蛇精病",
                "key":  "mpGuide04"
            }
          ]
    }
    '''
class Menu(object):
    def __init__(self):
        pass
    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()
        
    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

if __name__ == '__main__':
    myMenu = Menu()
    accessToken = Basic().get_access_token()
    #myMenu.delete(accessToken)
    myMenu.create(menuJson, accessToken)