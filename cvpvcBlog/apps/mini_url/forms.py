#-*- coding: utf-8 -*-

from django import forms
from .models import MiniURL

class MiniURLForm(forms.ModelForm):
    class Meta:
        model = MiniURL
        fields = ['long_url', 'pseudo']

    def __init__(self, *args, **kwargs):
        super(MiniURLForm, self).__init__(*args, **kwargs)
        self.fields['long_url'].widget.attrs.update({'class' : 'form-control'})
        self.fields['pseudo'].widget.attrs.update({'class' : 'form-control'})