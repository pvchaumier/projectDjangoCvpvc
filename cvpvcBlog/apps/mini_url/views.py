#-*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

import requests
from bs4 import BeautifulSoup

from .forms import MiniURLForm
from .models import MiniURL

class IndexView(generic.ListView):
    """
        View that manages what the user sees when arriving on the url shortener
    """
    model = MiniURL
    template_name = 'mini_url/welcome_page.html'
    context_object_name = 'latest_mini_url_list'

    def get_queryset(self):
        """
            Returns the last 5 url shortened
        """
        return MiniURL.objects.order_by('-date_creation')[:5]

class FullListView(generic.ListView):
    """
        View that sends all the shortened URLs orderer by date
    """
    model = MiniURL
    template_name = 'mini_url/full_list.html'
    context_object_name = 'full_mini_url_list'

    def get_queryset(self):
        """
            Returns the last 5 url shortened
        """
        return MiniURL.objects.order_by('-date_creation')

def new_url(request):
    """
        Form to get a new url and process data sent.
    """
    if request.method == 'POST':
        form = MiniURLForm(request.POST)

        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            pseudo = form.cleaned_data['pseudo']

            miniurl = MiniURL()
            miniurl.long_url = long_url
            miniurl.pseudo = pseudo

            try:
                res = requests.get(miniurl.long_url)
            except:
                miniurl.title = 'Page Not Found'
            else:
                if res.status_code != 200:
                    miniurl.title = 'Page Not Found'
                else:
                    try:
                        soup = BeautifulSoup(res.content)
                    except:
                        miniurl.title = 'Page Not Found'
                    else:
                        miniurl.title = soup.title.string

            miniurl.save()

            status = 'URL saved'

        else:
            status = 'Remplissez correctement le formulaire'

    else:
        form = MiniURLForm(label_suffix='')

    template_name = 'mini_url/miniurl_form.html'
    return render(request, template_name, locals())

def short(request, code):
    """
        View that redirects to the link or to 404 error page
    """
    miniurl = get_object_or_404(MiniURL, code=code)
    miniurl.nb_of_access += 1
    miniurl.save()
    return redirect(miniurl.long_url)
