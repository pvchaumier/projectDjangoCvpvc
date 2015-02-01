#-*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Article, Category, Comment

class IndexView(generic.ListView):
    """
        Welcome page with the list of all the different articles
    """
    model = Article
    template_name = 'article/index.html'
    context_object_name = 'articles_list'

    def get_queryset(self):
        """
            returns the list of all articles
        """
        return Article.objects.order_by('-publication_date')[:10]

class ArticleListView(generic.ListView):
    """
        Welcome page with the list of all the different articles
    """
    model = Article
    template_name = 'article/articles_list.html'
    context_object_name = 'articles_list'

    def get_queryset(self):
        """
            returns the list of all articles
        """
        return Article.objects.order_by('-publication_date')

class ArticleDetailView(generic.DetailView):
    """
        Detail of the article number pk
    """
    model = Article
    template_name = 'article/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        """
            Customization of the function to save the number of views
        """
        art = super(ArticleDetailView, self).get_object(queryset)
        art.nb_of_view += 1
        art.save()
        return art

class CategoriesListView(generic.ListView):
    """
        List of all categories
    """
    model = Category
    template_name = 'article/categories_list.html'
    context_object_name = 'categories_list'

    def get_queryset(self):
        """
            returns the list of all categories
        """
        return Category.objects.all()

class CategoryArticleListView(generic.ListView):
    """
        List of all article within one category
    """
    model = Article
    template_name = 'article/cate_articles_list.html'
    context_object_name = 'cate_article_list'

    def get_queryset(self):
        """
            returns the list of all categories
        """
        return Article.objects.filter(
            category__simplified_name=self.kwargs['cate_simplified_name'])

    def get_context_data(self, **kwargs):
        """
            adding the category object to the context variables
        """
        context = super(CategoryArticleListView, self).get_context_data(
            **kwargs)
        context['category'] = Category.objects.get(
            simplified_name=self.kwargs['cate_simplified_name'])
        return context
