from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProfileSerializer, PostSerializer

# Create your views here.
def index(request):
    return render(request,'index.html')

def index(request):
    return render(request,'signin.html')

def index(request):
    return render(request,'signup.html')

def index(request):
    return render(request,'setting.html')

def index(request):
    return render(request,'search.html')

def index(request):
    return render(request,'profile.html')

