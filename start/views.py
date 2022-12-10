import os

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
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
def profile(request):
    student = Student.objects.get(user = request.user)
    if student.exists():
        content = {
            "type" : "student",
            "student" : student,
            "user": request.user
        }

    organization = Organization.objects.get(user = request.user)
    if organization.exists():
        content = {
            "type": "organization",
            "organization" : organization,
            "user": request.user
        }
    return render(request, 'start/students.html',content)

@login_required(login_url='/login')
def cangeProfile(request):
    user = request.user
    organization = Organization.objects.get(user = user)
    if organization.exists():
        if request.method == "POST":
                form = changeOrganizationForm(request.POST)
                if form.is_valid():
                    cd = form.cleaned_data
                    user.username = cd["username"]
                    user.email = cd["email"]
                    user.phone = cd["phone"]
                    organization.name = cd['name']
                    organization.INN = cd["INN"]
                    organization.save()
                    user.save()
                    return redirect('profile')
        form = changeOrganizationForm(phone=user.phone, name = organization.name, INN = organization.INN,
                                 email=user.email, username=user.username)
        content = {
            "type": "organization",
            "form" : form,
        }
    student = Student.objects.get(user=user)
    if student.exists():
        if request.method == "POST":
                form = changeStudentForm(request.POST, request.FILES)
                if form.is_valid():
                    cd = form.cleaned_data
                    user.first_name = cd["first_name"]
                    user.last_name = cd["last_name"]
                    user.username = cd["username"]
                    user.email = cd["email"]
                    user.phone = cd["phone"]
                    student.image = cd["image"]
                    student.tags = cd["tags"]
                    student.CV = cd["CV"]
                    student.education = cd["education"]
                    student.department = cd["department"]
                    student.hardskill_softskill = cd["hardskill_softskill"]
                    student.experience = cd["experience"]
                    user.save()
                    student.save()
                    return redirect('profile')
        form = changeStudentForm(first_name=user.first_name, last_name=user.last_name, phone=user.phone,
                                 email=user.email, username=user.username, image=students.image, tags=students.tags,
                                 CV=students.CV, education=students.education, department=students.department,
                                 hardskill_softskill=students.hardskill_softskill,
                                 experience=students.experience )
        content = {
            "type": "student",
            "form" : form,
        }
    return render(request, 'start/students.html',content)

@login_required(login_url='/login')
def projects(request):
    projects = Project.objects.all()
    content = {
        "projects" : projects,
    }
    return render(request, 'start/students.html',content)

@login_required(login_url='/login')
def getProject(request,pk):
    project = Project.objects.get(pk)
    content = {
        "project" : project,
    }
    return render(request, 'start/students.html',content)

@login_required(login_url='/login')
def addProject(request):
    organization = Organization.objects.get(user = request.user)
    if organization.exists():
        if request.method == "POST":
            form = addProjectForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                newContactPerson = ContactPerson(name = cd["contactPersonName"],email = cd["contactPersonEmail"], phone = cd["contactPersonPhone"]).save()
                newProject = Project()
                newProject.name = cd["name"]
                newProject.definitions = cd["definitions"]
                newProject.budjet = cd["budjet"]
                newProject.dedlines = cd["dedlines"]
                newProject.positions = cd["positions"]
                newProject.techDocument = cd["techDocument"]
                newProject.goalOfProject = cd["goalOfProject"]
                newProject.background = cd["background"]
                newProject.result = cd["result"]
                newProject.criterias = cd["criterias"]
                newProject.organization = organization
                newProject.contactPerson = newContactPerson
                newProject.save()
                if cd["tags"]:
                    newProject.tags = cd["tags"]
                else:
                    newProject.tags = None
                newProject.save()
                redirect('projects')
        form = addProjectForm()
        content = {
            "form": form,
        }
        return render(request, 'start/addProject.html', content)
    else:
        messages.error(request,'Нет прав доступа')
        return redirect('login')