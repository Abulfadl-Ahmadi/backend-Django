from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('post/', PostList.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post/create/', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
]
