# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    url(r'^$', 
        views.IndexView.as_view(), 
        name='index'),
    url(r'^articles$', 
        views.ArticleListView.as_view(), 
        name='article_list'),
    url(r'^articles/(?P<pk>\d+)$', 
        views.ArticleDetailView.as_view(), 
        name='detail'),
    url(r'^categories/$', 
        views.CategoriesListView.as_view(), 
        name='category_list'),
    url(r'^categories/(?P<cate_simplified_name>[a-zA-Z0-9_]+)', 
        views.CategoryArticleListView.as_view(), 
        name='cate_article_list'),
)