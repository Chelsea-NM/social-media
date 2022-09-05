from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProfileSerializer, PostSerializer
from .models import Profile, Post, LikePost, FollowersCount


# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def setting(request):
    return render(request,'setting.html')

def search(request):
    return render(request,'search.html')

def profile(request):
    return render(request,'profile.html')

class ProfileViewSet(viewsets.ModelViewSet):
   queryset = Profile.objects.all()
   serializer_class = ProfileSerializer

class PostViewSet(viewsets.ModelViewSet):
   queryset = Post.objects.all()
   serializer_class = PostSerializer