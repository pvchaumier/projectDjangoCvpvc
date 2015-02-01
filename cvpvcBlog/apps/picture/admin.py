#-*- coding: utf-8 -*-

from django.contrib import admin
from .models import Picture

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(Picture, PictureAdmin)