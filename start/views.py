import os
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, redirect

def start(request):
    if (request.user.is_authenticated):
        return redirect('/students')
    return render(request, 'start/start.html')

@login_required(login_url='/login')
def students(request):
    students = Student.objects.all()
    # Доделать
    # userID = []
    # for student in students:
    #     userID.append(student.user.id)
    # user = User.objects.filter(id__in = userID).values('first_name', 'last_name')
    content = {
        "students" : students,
    }
    return render(request, 'start/students.html',content)

@login_required(login_url='/login')
def getStudent(request,pk):
    student = Student.objects.get(id = pk)
    content = {
        "student" : student,
    }
    return render(request, 'start/curstudent.html',content)

@login_required(login_url='/login')
def cangeStudent(request,pk):
    student = Student.objects.get(pk)
    content = {
        "student" : student,
    }
    return render(request, 'start/students.html',content)