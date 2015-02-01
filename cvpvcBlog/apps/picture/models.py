# -*- coding: utf-8 -*-

from django.db import models

class Picture(models.Model):
    """
        picture management logic is going to be defined here.
    """
    title = models.CharField(
        max_length=255, 
        unique=True,
        verbose_name='Titre de l\'image',)
    image = models.ImageField(upload_to='img/')

    def __unicode__(self):
        return u'{}'.format(self.title)
