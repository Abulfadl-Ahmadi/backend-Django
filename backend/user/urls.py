from django.urls import path
from user.views import *

urlpatterns = [
    path('users', ListUser.as_view(), name='users'),
    path('user/<int:pk>/', DetailUser.as_view(), name='user-detail'),
    # path('users/create/', CreateUser.as_view(), name='user-create'),
    path("user/create", register_request, name="user-create"),
    path('user/<int:pk>/update/', UpdateUser.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', DeleteUser.as_view(), name='user-delete'),
    path("user/login", login_request, name="user-login"),





]
