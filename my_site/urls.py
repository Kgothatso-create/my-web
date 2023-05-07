from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from .models import Blog

urlpatterns = [
    path("", views.home, name="index"),
    path("cv/", views.cv, name="cv"),
    path( 'blog/',ListView.as_view(queryset=Blog.objects.all().order_by("-date")[:25],template_name="blog.html"), name="blog"),
    path('post/<int:pk>/', DetailView.as_view(model = Blog,template_name="post.html"), name="post" ),
]
