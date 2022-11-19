from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import *


class CreateUser(CreateView):
    # model = Profile
    # fields =
    pass


class UpdateUser(UpdateView):
    pass


class DeleteUser(DeleteView):
    pass


class DetailUser(DetailView):
    queryset = CustomUser.objects.all()
    template_name = 'user/detail.html'
    context_object_name = "user"
    pk_url_kwarg = 'pk'


class ListUser(ListView):
    queryset = CustomUser.objects.all()
    template_name = 'user/list.html'
    context_object_name = "users"
