from django.conf.urls import url
from gsp import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^cats/', views.cats, name='cats'),
	url(r'about/$', views.about, name='about'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', 
	views.show_category, 
	name='show_category'),
	]