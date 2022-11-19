from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
# from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .forms import PostForm
from utils.utils import StatusOfPost


def Home(request):
    return render(request, 'index.html')


class PostList(ListView):
    queryset = Post.objects.filter(status="P")
    template_name = "post/list.html"
    context_object_name = "posts"


class PostDetail(DetailView):
    queryset = Post.objects.all()
    template_name = "post/detail.html"
    context_object_name = "post"
    pk_url_kwarg = "pk"


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'content', 'image', 'slug', 'user']
    template_name = "post/create.html"
    success_url = reverse_lazy("post-list")


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "post/update.html"
    success_url = reverse_lazy("post-list")
    pk_url_kwarg = "pk"


class PostDelete(DeleteView):
    model = Post
    template_name_suffix = "_confirm_delete"
    success_url = reverse_lazy("post-list")
    pk_url_kwarg = "pk"


# class PostListCreateAPIView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = ProductSerializer
