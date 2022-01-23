from django.shortcuts import render
from rest_framework import generics
from .models import Blog,Categories,Profile
from .serializers import BolgSerializers,CategoriesSerializer,UserRegisterSerializer
# Create your views here.
from django.contrib.auth.models import User

class UserRegisterApi(generics.CreateAPIView):
    queryset = User
    serializer_class = UserRegisterSerializer

class CategoriesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categories.objects.filter(is_deleted = False)
    serializer_class = CategoriesSerializer


class CategoriesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer




class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.filter(is_deleted = False)
    serializer_class = BolgSerializers

class BlogUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.filter(is_deleted =False)
    serializer_class = BolgSerializers



def index(request):
    print(request.GET['my_name'])
    return render(request, 'mobile/index.html')