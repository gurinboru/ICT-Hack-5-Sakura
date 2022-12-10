import datetime

from django.contrib.auth.models import User
from django.db import models

def userPhoto_directory_path(instance, filename):
    time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    time = str(time)
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'students/photo/' + filename + time

def usertechDocument_directory_path(instance, filename):
    time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    time = str(time)
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'techdocument/' + filename + time

def userpresentationDocument_directory_path(instance, filename):
    time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    time = str(time)
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'presentation/' + filename + time

class StatusApproval(models.Model):
    Agreed = 'Согласовано'
    ToBeAgreed = 'На согласовании'
    Denied = 'Отказано'
    CHOICES = (
        (Agreed, 'Согласовано'),
        (ToBeAgreed, 'На согласовании'),
        (Denied, 'Отказано')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'StatusApproval'
        verbose_name = 'StatusApproval'
        verbose_name_plural = 'StatusApproval'

        def __str__(self):
            return self.status

class StatusProject(models.Model):
    CHOICES = (
        ('Открыта', 'Открыта'),
        ('Закрыта', 'Закрыта'),
        ('Заморожена', 'Заморожена')
    )
    status = models.CharField(choices=CHOICES, max_length=300)

    class Meta:
        db_table = 'StatusProject'
        verbose_name = 'StatusProject'
        verbose_name_plural = 'StatusProject'

        def __str__(self):
            return self.status


# Сущности ----------------------------------------------

class Project(models.Model):
    name = models.TextField()
    definitions = models.TextField()
    budjet = models.IntegerField()
    dedlines = models.IntegerField()
    positions = models.TextField()
    techDocument = models.FileField(upload_to=usertechDocument_directory_path)
    goalOfProject = models.TextField()
    background = models.TextField()
    result = models.TextField()
    criterias = models.TextField()
    tags = models.TextField(null=True)
    id_status = models.ForeignKey('start.StatusProject',on_delete=models.DO_NOTHING,db_column='id_status')
    status_approval = models.ForeignKey(StatusApproval,on_delete=models.DO_NOTHING)
    organization = models.ForeignKey('start.Organization',on_delete=models.DO_NOTHING)
    contactPerson = models.ForeignKey('start.ContactPerson',on_delete=models.DO_NOTHING,null=True)

    class Meta:
        db_table = 'Projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class ContactPerson(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()

class Rialto(models.Model):
    student = models.ForeignKey("start.Student",on_delete=models.CASCADE)
    definitions = models.TextField()
    presentation = models.FileField(upload_to=userpresentationDocument_directory_path)
    status_approval = models.ForeignKey(StatusApproval,on_delete=models.DO_NOTHING)

class Organization(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.TextField()
    INN = models.IntegerField(null=True)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.TextField(null=True)
    image = models.ImageField(upload_to=userPhoto_directory_path,default='default/photo_2022-12-10_14-15-39.jpg')
    tags = models.TextField(null=True)
    ISU = models.IntegerField(null=True)
    CV = models.FileField(null=True)
    education = models.TextField(null=True)
    department = models.TextField(null=True)
    hardskill_softskill = models.TextField(null=True)
    experience = models.TextField(null=True)

class ApprovalPermission(models.Model):
    organization = models.ForeignKey("start.Organization",on_delete=models.CASCADE)
    field = models.TextField()
    statusApproval = models.ForeignKey(StatusApproval,on_delete=models.DO_NOTHING)

class StudentProject(models.Model):
    students = models.ForeignKey("start.Student",on_delete=models.DO_NOTHING)
    project = models.ForeignKey("start.Project",on_delete=models.DO_NOTHING)
    statusApproval = models.ForeignKey(StatusApproval, on_delete=models.DO_NOTHING)
