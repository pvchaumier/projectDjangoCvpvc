#-*- coding: utf-8 -*-

from django.contrib import admin
from .models import Article, Comment, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'last_edited', 'nb_of_view')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'pseudo', 'publication_date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'simplified_name')
    exclude = ('simplified_name',)

admin.site.register(Article, ArticleAdmin) 
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
