import os
from functools import reduce
from operator import and_, or_

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import *
from .forms import *
from django.shortcuts import render, redirect

def start(request):
    if (request.user.is_authenticated):
        return redirect('/students')
    return render(request, 'start/start.html')

@login_required(login_url='/login')
def students(request):
    students = Student.objects.all().only('education','user__first_name','user__last_name','image')
    content = {
        "students" : students,
    }
    try:
        organization = Organization.objects.get(user=request.user)
        content["type"] = "organization"
    except Organization.DoesNotExist:
        content["type"] = "student"
    return render(request, 'start/students.html',content)

@login_required(login_url='/login')
def getStudent(request,pk):
    student = Student.objects.get(id=pk)
    try:
        organization = Organization.objects.get(user=request.user)
        # permission = ApprovalPermission.objects.filter(organization = organization)
        # raw = 'SELECT '
        # for perm in permission:
        #     raw = raw + perm.field + ","
        # raw = raw + 'FROM start.student Where id = ' + str(pk)
        # student = Student.objects.raw(raw)

        content = {
            "student": student,
        }
        content["type"] = "organization"
    except Organization.DoesNotExist:
        content = {
            "student": student,
        }
        content["type"] = "student"
    return render(request, 'start/curstudent.html',content)

@login_required(login_url='/login')
def profile(request):
    user = User.objects.get(id = request.user.id)
    try:
        student = Student.objects.get(user = request.user)
        content = {
            "type" : "student",
            "student" : student,
            "user": request.user
        }

    except Student.DoesNotExist:
        try:
            organization = Organization.objects.get(user = user)
            content = {
                "type": "organization",
                "organization" : organization,
                "user": request.user
            }
        except Organization.DoesNotExist:
            messages.error(request,'?????????????????? ????????????')
            redirect("404")
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
                    student.ISU = cd["ISU"]
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
                "ISU": student.ISU,
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
    projects = Project.objects.filter(status_approval = StatusApproval.objects.get(status = StatusApproval.Agreed))
    try:
        student = Student.objects.get(user=user)
        if student.tags != None and student.tags != "":
            tags = student.tags.replace(",","").split(' ')
            recommendprojects = Project.objects.filter(reduce(or_, [Q(tags__icontains=tag) for tag in tags]), status_approval = StatusApproval.objects.get(status = StatusApproval.Agreed))
            content = {
                "type":"student",
                "recommendprojects": recommendprojects,
                "projects": projects,
            }
        else:
            content = {
                "type": "student",
                "projects": projects,
            }
        return render(request, 'start/projects.html', content)
    except Student.DoesNotExist:
        content = {
            "type": "organization",
            "projects" : projects,
        }
    return render(request, 'start/projects.html',content)

@login_required(login_url='/login')
def get_cv(request,pk):
    student = Student.objects.get(pk = pk)
    try:
        from django.http import FileResponse
        pathHelp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/', student.CV.name)
        return FileResponse(open(pathHelp, 'rb'))
    except FileNotFoundError:
        from django.http import Http404
        raise Http404()

@login_required(login_url='/login')
def get_presentation(request,pk):
    rialto = Rialto.objects.get(pk = pk)
    try:
        from django.http import FileResponse
        pathHelp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/', rialto.presentation.name)
        return FileResponse(open(pathHelp, 'rb'))
    except FileNotFoundError:
        from django.http import Http404
        raise Http404()

@login_required(login_url='/login')
def get_image(request,pk):
    student = Student.objects.get(pk = pk)
    try:
        from django.http import FileResponse
        pathHelp = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/', student.image.urls)
        return FileResponse(open(pathHelp, 'rb'))
    except FileNotFoundError:
        from django.http import Http404
        raise Http404()

@login_required(login_url='/login')
def getProject(request,pk):
    project = Project.objects.get(id = pk)
    user = User.objects.get(id = request.user.id)
    try:
        organization = Organization.objects.get(user=user)
        if project.organization == organization:
            seekStudent = StudentProject.objects.filter(project = project).values('students')
            if project.tags != None and project.tags != "":
                tags = project.tags.replace(",", "").split(' ')
                recommendstudent = Student.objects.filter(reduce(or_, [Q(tags__icontains=tag) for tag in tags]))
                content = {
                    "type":"organization",
                    "recommendstudent" : recommendstudent,
                    "project": project,
                    "seekStudent":seekStudent
                }
            else:
                content = {
                    "seekStudent": seekStudent,
                    "type": "organization",
                    "project": project,
                }
        else:
            content = {
                "type": "organization",
                "project": project,
            }
            return render(request, 'start/curproject.html', content)
    except Organization.DoesNotExist:
        content = {
            "type": "student",
            "project" : project,
        }
    return render(request, 'start/curproject.html',content)

@login_required(login_url='/login')
def rialtos(request):
    rialtos = Rialto.objects.filter(status_approval = StatusApproval.objects.get(status = StatusApproval.Agreed))
    content = {
        "rialtos" : rialtos,
    }
    try:
        organization = Organization.objects.get(user=request.user)
        content["type"] = "organization"
    except Organization.DoesNotExist:
        content["type"] = "student"
    return render(request, 'start/rialtos.html',content)

@login_required(login_url='/login')
def getRialto(request,pk):
    rialto = Rialto.objects.get(pk = pk, status_approval = StatusApproval.objects.get(status = StatusApproval.Agreed))
    content = {
        "rialto" : rialto,
    }
    try:
        organization = Organization.objects.get(user=request.user)
        content["type"] = "organization"
    except Organization.DoesNotExist:
        content["type"] = "student"
    return render(request, 'start/currialto.html',content)

@login_required(login_url='/login')
def addRialto(request):
    user = User.objects.get(id=request.user.id)
    try:
        student = Student.objects.get(user=user)
        if request.method == "POST":
            form = addRialtoForms(request.POST, request.FILES)
            if form.is_valid():
                cd = form.cleaned_data
                newRialto = Rialto()
                newRialto.name = cd['name']
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
                messages.error(request,'???? ???????????????? ??????????')
                return redirect('rialtos')
        else:
            form = addRialtoForms()
            content = {
                "type": "student",
                "form": form,
            }
            return render(request, 'start/add_rialto.html',content)
    except Student.DoesNotExist:
        messages.error(request,'?????? ???????? ??????????????')
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
            "type" : 'organization',
            "form": form,
        }
        return render(request, 'start/add_project.html', content)
    except Organization.DoesNotExist:
        messages.error(request,'?????? ???????? ??????????????')
        return redirect('projects')


@login_required(login_url='/login')
def requestStudentToProject(request,pk):
    # if request.method == "POST":
        try:
            student = Student.objects.get(user=request.user)
            StudentProject(students = student, project = Project.objects.get(pk = pk),statusApproval =StatusApproval.objects.get(status = StatusApproval.ToBeAgreed)).save()
            messages.success(request, '???????? ???????????? ??????????????')
            return redirect("studentonproject")
        except Student.DoesNotExist:
            messages.error(request, '?????? ???????? ??????????????')
            return redirect('studentonproject')
    #return redirect('studentonproject')


@login_required(login_url='/login')
def studentOnProject(request):
    try:
        student = Student.objects.get(user=request.user)
        studentProject = StudentProject.objects.filter(students = student)
        rialtos = Rialto.objects.filter(student = student)
        content = {
            "type": 'student',
            "studentProject": studentProject,
            "rialtos": rialtos
        }
        return  render(request, 'start/studentonproject.html', content)
    except Student.DoesNotExist:
        messages.error(request, '?????? ???????? ??????????????')
        return redirect('students')

@login_required(login_url='/login')
def getMyProject(request):
    try:
        organization = Organization.objects.get(user=request.user)
        projects = Project.objects.filter(organization=organization)
        content = {
            "type": 'organization',
            "projects": projects,
        }
        return  render(request, 'start/getMyProject.html', content)
    except Organization.DoesNotExist:
        messages.error(request, '?????? ???????? ??????????????')
        return redirect('students')