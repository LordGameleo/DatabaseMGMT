from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

def start(request):
    return render(request,'start.html',{})
