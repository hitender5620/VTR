from cProfile import Profile
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms

def home(request):
    return render(request, "home.html")

class signupView(View):
    def get(self, request):
        fm = UserCreationForm()
        return render(request, "signup.html", {'form':fm})
    
class myloginView(View):
    def get(self, request):
        return render(request, "login.html")
    

def new_form(request):
    
    return render(request, "new_form.html")
 

