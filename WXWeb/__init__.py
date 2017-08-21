# -*- coding: utf-8-*-
import sys
sys.path.append('utils')
import urllib
import basic
import menu


wxMenu = menu.Menu()
wxBasic = basic.Basic()
accessToken = wxBasic.get_access_token()
#myMenu.delete(accessToken)
wxMenu.create(wxBasic.menuJson, accessToken)