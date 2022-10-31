from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Post


def Home(request):
    return render(request, 'index.html')


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = "post/list.html"
    context_object_name = "posts"


class PostDetail(DetailView):
    queryset = Post.objects.all()
    template_name = "post/detail.html"
    context_object_name = "post"
    pk_url_kwarg = "pk"


class PostUpdate(UpdateView):
    pass


class PostCreate(CreateView):
    pass


class PostDelete(DeleteView):
    pass
