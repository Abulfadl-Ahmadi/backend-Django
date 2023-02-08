from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
# from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post, Comment
from .forms import PostForm, CommentForm


# def Home(request):
#     return render(request, 'index.html')

def Home(request):
    context = { }
    return render(request, "index.html", context)


class PostList(ListView):
    queryset = Post.objects.filter(status="P")
    template_name = "post/list.html"
    context_object_name = "posts"
    paginate_by = 12


# class PostDetail(DetailView):
#     queryset = Post.objects.all()
#     template_name = "post/detail.html"
#     context_object_name = "post"
#     pk_url_kwarg = "pk"

class PostDetail(DetailView):
    template_name = "post/detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        connected_comments = Comment.objects.filter(
            CommentPost=self.get_object())
        number_of_comments = connected_comments.count()
        data['comments'] = connected_comments
        data['no_of_comments'] = number_of_comments
        data['comment_form'] = CommentForm()
        return data

    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            print(
                '-------------------------------------------------------------------------------Reached here')
            comment_form = CommentForm(self.request.POST)
            if comment_form.is_valid():
                content = comment_form.cleaned_data['content']
                try:
                    parent = comment_form.cleaned_data['parent']
                except:
                    parent = None

            new_comment = Comment(content=content, author=self.request.user,
                                  CommentPost=self.get_object(), parent=parent)
            new_comment.save()
            return redirect(self.request.path_info)



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
