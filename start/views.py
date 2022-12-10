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
    user = User.objects.get(id = request.user.id)
    # try:
    #     organization = Organization.objects.get(user = user)
    #     permission = ApprovalPermission.objects.filter(organization = organization)
    #     s = ''
    #     for perm in permission:
    #         s = s + '"' + perm.field + '",'
    #     students = Student.objects.all().values(s)
    # except Organization.DoesNotExist:
    students = Student.objects.all()
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
    user = User.objects.get(id = request.user.id)
    try:
        organization = Organization.objects.get(user = user)
        if request.method == "POST":
                form = changeOrganizationForm(request.POST)
                if form.is_valid():
                    cd = form.cleaned_data
                    user.username = cd["username"]
                    user.email = cd["email"]
                    organization.name = cd['name']
                    organization.INN = cd["INN"]
                    organization.save()
                    user.save()
                    return redirect('profile')
        form = changeOrganizationForm(initial={
            "name" : organization.name,
            "INN" : organization.INN,
            "email":user.email,
            "username":user.username})
        content = {
            "type": "organization",
            "form" : form,
        }
    except Organization.DoesNotExist:
        try:
            student = Student.objects.get(user=user)
            if request.method == "POST":
                form = changeStudentForm(request.POST, request.FILES)
                if form.is_valid():
                    cd = form.cleaned_data
                    user.first_name = cd["first_name"]
                    user.last_name = cd["last_name"]
                    user.email = cd["email"]
                    student.phone = cd["phone"]
                    if cd["image"] != None:
                        student.image = cd["image"]
                    student.tags = cd["tags"]
                    if cd["CV"] != None:
                        student.CV = cd["CV"]
                    student.education = cd["education"]
                    student.department = cd["department"]
                    student.hardskill_softskill = cd["hardskill_softskill"]
                    student.experience = cd["experience"]
                    user.save()
                    student.save()
                    return redirect('profile')
            form = changeStudentForm(initial={
                "first_name":user.first_name,
                "last_name":user.last_name,
                "phone":student.phone,
                "email":user.email,
                "image":student.image,
                "tags":student.tags,
                "CV":student.CV,
                "education":student.education,
                "department":student.department,
                "hardskill_softskill":student.hardskill_softskill,
                "experience":student.experience })
            content = {
                "type": "student",
                "form" : form,
            }
        except Student.DoesNotExist:
            redirect('404')
    return render(request, 'start/profile.html',content)

@login_required(login_url='/login')
def projects(request):
    user = User.objects.get(id=request.user.id)
    projects = Project.objects.all()
    try:
        student = Student.objects.get(user=user)
        if student.tags != None:
            tags = student.tags.replace(",","").split(' ')
            recommendprojects = Project.objects.filter(tags__icontains= tags)
            content = {
                "recommendprojects": recommendprojects,
                "projects": projects,
            }
            return render(request, 'start/projects.html', content)
    except Student.DoesNotExist:
        content = {
            "projects" : projects,
        }
    content = {
        "projects": projects,
    }
    return render(request, 'start/projects.html',content)

@login_required(login_url='/login')
def getProject(request,pk):
    project = Project.objects.get(pk)
    user = User.objects.get(id = request.user.id)
    try:
        organization = Organization.objects.get(user=user)
        if project.tags != None and project.organization == organization :
            tags = project.tags.replace(",", "").split(' ')
            recommendstudent = Student.objects.filter(tags__icontains=tags)
            content = {
                "recommendstudent" : recommendstudent,
                "project": project,
            }
    except Organization.DoesNotExist:
        content = {
            "project" : project,
        }
    return render(request, 'start/curproject.html',content)

@login_required(login_url='/login')
def rialtos(request):
    rialtos = Rialto.objects.all()
    content = {
        "rialtos" : rialtos,
    }
    return render(request, 'start/rialtos.html',content)

@login_required(login_url='/login')
def getRialto(request,pk):
    rialto = Rialto.objects.get(pk)
    content = {
        "rialto" : rialto,
    }
    return render(request, 'start/get_rialto.html',content)

@login_required(login_url='/login')
def addRialto(request):
    user = User.objects.get(id=request.user.id)
    try:
        student = Student.objects.get(user=user)
        if request.method == "POST":
            form = addRialto(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                newRialto = Rialto()
                newRialto.student = student
                newRialto.definitions = cd['definitions']
                newRialto.dedline = cd['dedline']
                newRialto.FCF = cd['FCF']
                newRialto.investment = cd['investment']
                if cd['presentation'] != None:
                    newRialto.presentation = cd['presentation']
                newRialto.status_approval = StatusApproval.objects.get(status=StatusApproval.ToBeAgreed)
                newRialto.save()
                return redirect('rialtos')
        else:
            form = addRialto()
            content = {
                "form": form,
            }
            return render(request, 'start/add_rialto.html',content)
    except Student.DoesNotExist:
        messages.error(request,'Нет прав доступа')
        return redirect('rialtos')

@login_required(login_url='/login')
def addProject(request):
    try:
        organization = Organization.objects.get(user = request.user)
        if request.method == "POST":
            form = addProjectForm(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                newContactPerson = ContactPerson()
                newContactPerson.name = cd["contactPersonName"]
                newContactPerson.email = cd["contactPersonEmail"]
                newContactPerson.phone = cd["contactPersonPhone"]
                newContactPerson.save()

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
                newProject.status_approval = StatusApproval.objects.get(status = StatusApproval.ToBeAgreed)
                newProject.id_status = StatusProject.objects.get(status = StatusProject.OPEN)
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
        return render(request, 'start/add_project.html', content)
    except Organization.DoesNotExist:
        messages.error(request,'Нет прав доступа')
        return redirect('projects')


@login_required(login_url='/login')
def requestStudentToProject(request,pk):
    if request.method == "POST":
        try:
            student = Student.objects.get(user=request.user)
            StudentProject(students = student, projects = Project.objects.get(pk = pk),statusApproval =StatusApproval.objects.get(status = StatusApproval.ToBeAgreed)).save()
            messages.success(request, 'Ваша заявка принята')
            redirect("projects")
        except Student.DoesNotExist:
            messages.error(request, 'Нет прав доступа')
            return redirect('projects')
    return redirect('projects')