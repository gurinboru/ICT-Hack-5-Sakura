import os
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect

def start(request):
    if (request.user.is_authenticated):
        return redirect('/students')
    return render(request, 'start/start.html')

@login_required(login_url='/login')
def getCandidates(request):
    students = Student.objects.all()
    content = {
        "students" : students
    }
    return render(request, 'start/students.html',content)