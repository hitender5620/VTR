from cProfile import Profile
from http.client import HTTPResponse
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from posts.form import myloginForm, signupForm
from . import *

def home(request):
    return render(request, "home.html")

class signupView(View):
    def get(self, request):
        fm = signupForm()
        return render(request, "signup.html", {'form':fm})
    def post(self, request):
        fm = signupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Sign Up Success !")
            return redirect('/signup')
        else:
            return render(request, "signup.html", {'form':fm})
        
class myloginView(View):
    def get(self, request):
        fm = myloginForm()
        return render(request, "login.html", {'form':fm})
    def post(self, request):
        fm = myloginForm(request,data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            
            user = authenticate(request, username=username, password= password)
            if user is not None:
                login(request,user)
                return redirect('home')
        else:
            return render(request, "login.html", {'form':fm})
        
        
        
    