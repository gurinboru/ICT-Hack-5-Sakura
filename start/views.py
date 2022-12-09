import os
from django.shortcuts import render, redirect

def start(request):
    return render(request, 'start/start.html')