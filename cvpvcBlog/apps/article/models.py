# -*- coding: utf-8 -*-

import re

from django.db import models

class Article(models.Model):
    """
        A very simple model for articles that contains only the title,
        the content and the date of publication
    """
    title = models.CharField(max_length=255, unique_for_date='publication_date', verbose_name='Titre de l\'article')
    publication_date = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Date d\'ajout')
    last_edited = models.DateField(auto_now=True, auto_now_add=True, verbose_name='Dernière modification')
    content = models.TextField(verbose_name='Contenu de l\'article')
    nb_of_view = models.PositiveIntegerField(default=0 ,verbose_name='Nombre de vues')
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return '{title} - {publication_date}'.format(title=self.title, publication_date=self.publication_date)

class Comment(models.Model):
    """
        Simple comment model. Only I will be able to had comment for now
    """
    article = models.ForeignKey('Article')
    pseudo = models.CharField(max_length=255, verbose_name='Pseudo')
    content = models.TextField(verbose_name='Contenu du commentaire')
    publication_date = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Date de publication')

class Category(models.Model):
    """
        Simple category for the articles
    """
    name = models.CharField(max_length=255, unique=True, verbose_name='Nom de la catégorie')
    simplified_name = models.CharField(max_length=254, verbose_name='Nom simplifié de la catégorie')

    def __unicode__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        if self.name:
            self.simplified_name = re.sub(r'[^a-zA-Z0-9_]', '_', self.name.lower())
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Catégorie'
