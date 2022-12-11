from django.urls import path
from user.views import *

urlpatterns = [
    path('users', ListUser.as_view(), name='users'),
    path('user/<int:pk>/', DetailUser.as_view(), name='user-detail'),
    path('user/<int:pk>/update/', UpdateUser.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', DeleteUser.as_view(), name='user-delete'),
    path('', followers_count, name="followers_count"),
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
]
