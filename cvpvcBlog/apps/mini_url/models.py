#-*- coding: utf-8 -*-

import random
import string

from django.db import models

class MiniURL(models.Model):
    """
        Model that takes the mini-URLs and save them
    """
    long_url = models.URLField(unique=True, verbose_name='Longue Url')
    code = models.CharField(unique=True, max_length=200, verbose_name='Code pour identifier l\'URL')
    date_creation = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Date de creation du lien')
    pseudo = models.CharField(max_length=200, blank=True, verbose_name='Pseudo')
    title = models.CharField(max_length=200, blank=True, verbose_name='Titre de la page')
    nb_of_access = models.IntegerField(default=0, verbose_name='Nombre d\'accès au lien')

    def __unicode__(self):
        """
            The representation sends back the long URL and the code
        """
        return 'URL : {} - CODE : {}'.format(self.long_url, self.url_code)

    def save(self, *args, **kwargs):
        """
            Rewriting the save method to include the code generating
        """
        if self.pk is None:
            self.mixing_url(5)
        super(MiniURL, self).save(*args, **kwargs)

    def mixing_url(self, N):
        """
            Generate a string of size N and checks if it already exists
        """
        is_code_unique = False
        while not is_code_unique:
            char_to_use = list(string.ascii_letters + string.digits)
            random.shuffle(char_to_use)
            random_code = ''.join([letter for letter in char_to_use[:N]])
            try:
                MiniURL.objects.get(code=random_code)
            except MiniURL.DoesNotExist:
                self.code = random_code
                is_code_unique = True