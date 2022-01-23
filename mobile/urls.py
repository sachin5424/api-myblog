
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .models import UserViewSet
from .views import index,BlogListCreateAPIView,BlogUpdateDestroyAPIView,CategoriesListCreateAPIView,CategoriesRetrieveUpdateDestroyAPIView,UserRegisterApi
from .middleware.auth import simple_middleware

urlpatterns = [
    path('',simple_middleware(index)),
    path('api/register/', UserRegisterApi.as_view()),
    path('api/categories/', CategoriesListCreateAPIView.as_view()),
    path('api/blog/',BlogListCreateAPIView.as_view()),
    path('api/blog/<int:pk>',BlogUpdateDestroyAPIView.as_view()),
    path('api/categories/<int:pk>',CategoriesRetrieveUpdateDestroyAPIView.as_view()),
]