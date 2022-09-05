from datetime import datetime
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Profile, Post, FollowersCount


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user","bio","profileimg","bitool"]
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","user","image","caption","no_of_likes","created_at"]   
        