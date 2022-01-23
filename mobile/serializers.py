from rest_framework import serializers
from .models import Blog,Categories,Profile
from django.contrib.auth.models import User



class  UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password','username','first_name','last_name','email')



class CategoriesSerializer(serializers.ModelSerializer):
    # blog = serializers.StringRelatedField(many=True)
    class Meta:
        model = Categories
        fields = '__all__'

class BolgSerializers(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=False,read_only=False)
    class Meta:
        model = Blog
        fields = ['title','categories','dic']
    def create(self, validated_data):
        print(self)
        pass




