import os
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect

def start(request):
    if (request.user.is_authenticated):
        return redirect('/students')
    return render(request, 'start/start.html')

@login_required(login_url='/login')
def getStudent(request):
    students = Student.objects.all()
    user = User.objects.get(id = students.user)
    firstname = user.first_name
    lastname = user.last_name
    content = {
        "students" : students,
        "firstname":firstname,
        "lastname":lastname
    }
    return render(request, 'start/students.html',content)