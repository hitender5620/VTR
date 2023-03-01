from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms


def home(request):
    data={
        'title':'VIRTUAL TRIAL ROOM'
    }
    return render(request, "index.html",data)
  

 



    