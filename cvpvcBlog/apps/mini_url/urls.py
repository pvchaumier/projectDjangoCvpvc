#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from cvpvcBlog.apps.mini_url import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^full_list/', views.FullListView.as_view(), name='full_list'),
    url(r'^new_url/', views.new_url, name='new_url'),
    url(r'^(?P<code>[a-zA-Z0-9]*)', views.short, name='short'),
)