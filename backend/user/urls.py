from django.urls import path
from user.views import DetailUser, ListUser

urlpatterns = [
    path('users', ListUser.as_view(), name='users'),
    path('user/<int:pk>/', DetailUser.as_view(), name='user-detail'),


]
