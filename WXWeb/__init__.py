# -*- coding: utf-8-*-
import sys
sys.path.append('utils')
import urllib
from basic import Basic


myMenu = Menu()
accessToken = Basic().get_access_token()
#myMenu.delete(accessToken)
myMenu.create(basic.menuJson, accessToken)