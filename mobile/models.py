import datetime

from django.contrib.auth.models import User
from django.db import models
from rest_framework import routers, serializers, viewsets

# Create your models here.


Attribute_Type =[
    ('number', 'number'),
    ('select', 'select'),
    ('date', 'date'),
    ('text', 'text'),

]
Attribute_Type1 =[
    ('number', 'number'),
    ('select', 'select'),
    ('date', 'date'),
    ('text', 'text'),

]


class Categories(models.Model):
    title = models.CharField(max_length=100)
    parentId = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True)
    is_deleted = models.BooleanField(default=False,blank=False)
    def __str__(self):
        return  self.title

    def delete(self):
        Categories.objects.filter(pk=self.id).update(is_deleted=True)
        if not Blog.objects.filter(pk=self.id):
            pass
        Blog.objects.filter(categories=self.id).update(is_deleted=True)
        pass


class AttributeOption(models.Model):
    option_name= models.CharField(max_length=100)
    option_value=models.CharField(max_length=100)
    option_position = models.SmallIntegerField()
    def __str__(self):
        return  self.option_name




# name
# :
# Clothes Attributes
# status
# :
# active
# family_attribute
# :
# Array
# isActive
# :
# true
# isDeleted
# :
# false


class attributeFamilys(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    family_attribute = models.ManyToManyField('Attributes')
    isDeleted = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    def __str__(self):
        return  self.name



class Attributes(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=100,unique=True)
    type = models.CharField(max_length=100,default=1, choices=Attribute_Type)
    isConfigurable = models.BooleanField(default=False)
    options = models.ManyToManyField(AttributeOption)
    status = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return  self.title


class productAttribute(models.Model):
    attributeId  = models.ForeignKey(Attributes,on_delete=models.CASCADE)
    attribute_value = models.CharField(max_length=200)
    def __str__(self):
        return  self.attributeId.title


class Products(models.Model):
        parentId= models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True)
        productType: models.CharField(choices=Attribute_Type1 ,default=1)
        product_name = models.CharField(max_length=200)
        product_code = models.CharField(max_length=200,unique=True)
        categories = models.ManyToManyField(Categories)
        familyAtrributeId=  models.ForeignKey('Attributes',on_delete=models.CASCADE,null=True, blank=True)
        sku=  models.CharField(max_length=200,unique=True)
        description  = models.TextField()
        short_description= models.TextField()
        meta_title = models.TextField()
        meta_tags =models.TextField()
        meta_description= models.TextField()
        product_price = models.FloatField()
        productAttribute = models.ManyToManyField(productAttribute)
        inventory = models.SmallIntegerField()
        isActive = models.BooleanField(default=False)
        isDeleted  = models.BooleanField(default=False)
        relatedProducts =models.ManyToManyField('self')

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