#-*- coding: utf-8 -*-

from django.views import generic

from .models import Picture

class ImageView(generic.ListView):
    """
        This view is the gallery of the website with all the pictures taken.
    """
    model = Picture
    template_name = 'article/gallery.html'
    context_object_name = 'images'