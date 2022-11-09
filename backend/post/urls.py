from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('list/', PostList.as_view(), name='post-list'),
    path('list/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('list/create/', PostCreate.as_view(), name='post-create'),
    path('list/<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('list/<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
]
