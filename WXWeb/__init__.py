# -*- coding: utf-8-*-
import sys
sys.path.append('utils')
import basic
import menu



wxBasic = basic.Basic()
accessToken = wxBasic.get_access_token("","")
if accessToken != "":
	wxMenu = menu.Menu()
	#myMenu.delete(accessToken)
	wxMenu.create(menu.menuJson, accessToken)