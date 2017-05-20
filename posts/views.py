from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    template_name = 'posts/post_list.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post