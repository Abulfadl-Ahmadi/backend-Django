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
    pass


class ListUser(ListView):
    pass
