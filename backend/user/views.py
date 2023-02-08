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
from django.contrib.auth.models import auth


def index(request):
    current_user = request.GET.get('user')
    logged_in_user = request.user.username
    user_followers = len(FollowersCount.objects.filter(user=current_user))
    user_following = len(FollowersCount.objects.filter(follower=current_user))
    user_followers0 = FollowersCount.objects.filter(user=current_user)
    user_followers1 = []
    for i in user_followers0:
        user_followers0 = i.follower
        user_followers1.append(user_followers0)

    if logged_in_user in user_followers1:
        follow_button_value = 'unfollow'
    else:
        follow_button_value = 'follow'

    return render(request, 'user/detail.html', {
        'current_user': current_user,
        'user_followers': user_followers,
        'user_following': user_following,
        'follow_button_value': follow_button_value
    })
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
    paginate_by = 12


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
    return render(request=request, template_name="user/signup.html", context={"register_form": form})


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



# def follow(request):
#     if request.method == 'POST':
#         follower = request.POST['follower']
#         user = request.POST['user']

#         if FollowersCount.objects.filter(follower=follower, user=user).first():
#             delete_follower = FollowersCount.objects.get(follower=follower, user=user)
#             delete_follower.delete()
#             return redirect('/profile/'+user)
#         else:
#             new_follower = FollowersCount.objects.create(follower=follower, user=user)
#             new_follower.save()
#             return redirect('/profile/'+user)
#     else:
#         return redirect('/')
    