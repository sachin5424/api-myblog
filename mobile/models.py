import datetime

from django.contrib.auth.models import User
from django.db import models
from rest_framework import routers, serializers, viewsets

# Create your models here.





class Categories(models.Model):
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False,blank=False)
    def __str__(self):
        return  self.title

    def delete(self):
        Categories.objects.filter(pk=self.id).update(is_deleted=True)
        if not Blog.objects.filter(pk=self.id):
            pass
        Blog.objects.filter(categories=self.id).update(is_deleted=True)
        pass


class Blog(models.Model):
    categories = models.ForeignKey(Categories,related_name='Blog',on_delete=models.CASCADE,blank=True)
    title = models.CharField(max_length=200)
    dic = models.TextField()
    is_deleted = models.BooleanField(default=False, blank=False)
    def __str__(self):
        return  self.title





class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()
    is_deleted = models.BooleanField(default=False,blank=False)
    is_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.user.username

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class sendOtp(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.IntegerField()
    otp = models.SmallIntegerField()
    def __str__(self):
        return  self.user