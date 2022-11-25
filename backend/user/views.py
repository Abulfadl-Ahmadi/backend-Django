from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth import login, authenticate  # add this
from django.shortcuts import render, redirect
from django.contrib import messages
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


def register_request(request):
    if request.method == "POST":
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = CustomUserCreateForm()
    return render(request=request, template_name="user/create.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="user/login.html", context={"login_form": form})


@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")
