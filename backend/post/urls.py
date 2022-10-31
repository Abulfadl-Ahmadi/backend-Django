from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('list/', PostList.as_view(), name='post-list'),
    path('list/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
