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
    userID = []
    for student in students:
        userID.append(student.user.id)
    user = User.objects.filter(id__in = userID).values('first_name', 'last_name')
    content = {
        "students" : students,
        "user":user
    }
    return render(request, 'start/students.html',content)