# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^miniurl/', include('cvpvcBlog.apps.mini_url.urls', namespace='miniurl')),
    url(r'^', include('cvpvcBlog.apps.article.urls', namespace='blog')),
)