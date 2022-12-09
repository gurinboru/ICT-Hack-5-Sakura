import os
from django.shortcuts import render, redirect

def start(request):
    # if (request.user.is_authenticated):
    #     return redirect('/candidates')
    return render(request, 'start/start.html')