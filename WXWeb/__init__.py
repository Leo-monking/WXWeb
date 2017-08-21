# -*- coding: utf-8-*-
import sys
sys.path.append('utils')
import urllib
import Basic
import Menu


wxMenu = Menu()
basic = Basic()
accessToken = basic.get_access_token()
#myMenu.delete(accessToken)
wxMenu.create(basic.menuJson, accessToken)