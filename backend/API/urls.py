from django.urls import path, include
from .views import PostListAPIView, PostRetrieveUpdateDestroyAPIView, CustomUserViewSet


from API.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')



urlpatterns = [
    path("posts/",PostListAPIView.as_view(),name = "PostListAPIView"),
    path("posts/<int:pk>/", PostRetrieveUpdateDestroyAPIView.as_view(),
         name="PostRetrieveUpdateDestroyAPIView"),
    path("", include(router.urls), name='user-api'),

    
]
