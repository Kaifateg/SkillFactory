from django.views.generic import ListView, DetailView
from .models import *


class PostNews(ListView):
    template_name = 'post_news.html'
    context_object_name = 'postnews'
    queryset = Post.objects.filter(type_category='NW')
    ordering = '-time_create_post'

class PostNW(DetailView):
    queryset = Post.objects.filter(type_category='NW')
    template_name = 'post_nw.html'
    context_object_name = 'postnw'


