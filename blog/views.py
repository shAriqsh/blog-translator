from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.

class BlogView(generic.DetailView):
    model= Post
    template_name='blog.html'

class AboutView(generic.TemplateView): #TemplateView is used for views that simply render a template without getting data from the model
    template_name='about.html'

class PostList(generic.ListView):
    queryset= Post.objects.filter(status=1).order_by('-date_created') # "-" signifies that the newest blogs created will be visible first
    template_name='index.html'