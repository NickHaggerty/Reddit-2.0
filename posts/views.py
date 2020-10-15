from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    login_url = 'login' 

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    login_url = 'login' 

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body',)
    template_name = 'post_edit.html'
    login_url = 'login'

    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    login_url = 'login'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields - ('title', 'body', 'author')
