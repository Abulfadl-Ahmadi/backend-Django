from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *


class CreateUser(CreateView):
    model = CustomUser
    template_name = 'user/create.html'
    form_class = CustomUserCreateForm
    success_url = reverse_lazy("users")


class UpdateUser(UpdateView):
    model = CustomUser
    template_name = 'user/update.html'
    form_class = CustomUserUpdateForm
    success_url = reverse_lazy("users")
    pk_url_kwarg = "pk"


class DeleteUser(DeleteView):
    model = CustomUser
    template_name_suffix = "_confirm_delete"
    success_url = reverse_lazy("users")
    pk_url_kwarg = "pk"


class DetailUser(DetailView):
    queryset = CustomUser.objects.all()
    template_name = 'user/detail.html'
    context_object_name = "user"
    pk_url_kwarg = 'pk'


class ListUser(ListView):
    queryset = CustomUser.objects.all()
    template_name = 'user/list.html'
    context_object_name = "users"
