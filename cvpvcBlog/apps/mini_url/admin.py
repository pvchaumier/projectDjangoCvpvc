#-*- coding: utf-8 -*-

from django.contrib import admin
from cvpvcBlog.apps.mini_url.models import MiniURL

class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'title', 'code', 'date_creation', 'pseudo', 'nb_of_access')

admin.site.register(MiniURL, MiniURLAdmin)