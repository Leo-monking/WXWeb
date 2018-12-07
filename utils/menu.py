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
            "name":"微金融",
            "sub_button":
            [
                {
                    "type":"click",
                    "name":"账户信息即时通",
                    "key":"V1001_ALERT"
                },
                {
                    "type":"click",
                    "name":"云管家",
                    "key":"V1001_HELP"
                },
                {
                    "type":"click",
                    "name":"我的账户",
                    "key":"V1001_HELP"
                },
                {
                    "type":"click",
                    "name":"我要开户",
                    "key":"V1001_HELP"
                }
            ]
        },
        {
            "name":"悦理财",
            "sub_button":
            [
                {
                    "type":"view",
                    "name":"直销银行",
                    "url":"http://www.systex.com.tw/"
                },
                {
                    "type":"view",
                    "name":"理财超市",
                    "url":"http://www.splunk.com/"
                },
                {
                    "type":"view",
                    "name":"信用卡服务",
                    "url":"http://www.splunklab.com/"
                },
                {
                    "type":"view",
                    "name":"优房闪贷",
                    "url":"http://www.splunklab.com/"
                },
                {
                    "type":"view",
                    "name":"手机银行下载",
                    "url":"http://www.splunklab.com/"
                }
            ]
        },
        {
            "name":"慧生活",
            "sub_button":
            [
                {
                    "type":"click",
                    "name":"智能客服",
                    "key":"V1001_SYSTEX"
                },
                {
                    "type":"click",
                    "name":"网点服务",
                    "key":"V1001_huabei"
                },
                {
                    "type":"click",
                    "name":"推荐有奖",
                    "key":"V1001_huadong"
                },
                {
                    "type":"click",
                    "name":"话费重置",
                    "key":"V1001_huanan"
                },
                {
                    "type":"click",
                    "name":"天天特惠",
                    "key":"V1001_hongkong"
                }
            ]
        }
    ]
 }'''

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
