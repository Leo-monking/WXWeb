from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
from handle import views as handle_views
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$',learn_views.index),
	url(r'^wx$',handle_views.index),
]
