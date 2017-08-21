# -*- coding: utf-8 -*-
'''
    Created on 2017-8-20
    @author: MONKING
    
    内容描述：
    	定义访问WXWeb的URL匹配模式
'''

from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
from handle import views as handle_views
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$',learn_views.index),
	url(r'^wx$',handle_views.index),
]
