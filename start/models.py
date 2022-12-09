from django.contrib.auth.models import User
from django.db import models


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
    techDocument = models.FileField()
    goalOfProject = models.TextField()
    background = models.TextField()
    result = models.TextField()
    criterias = models.TextField()
    id_status = models.ForeignKey('start.StatusProject',on_delete=models.DO_NOTHING,db_column='id_status')
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'Projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     self.id_status = StatusJob.objects.get(pk=0)
    #     super().save(*args,**kwargs)
def userCV_directory_path(instance, filename):
    return 'candidate/CV/' + filename

def userPhoto_directory_path(instance, filename):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'candidate/photo/' + filename


class ContactPerson(models.Model):
    organization = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.TextField()
    email = models.EmailField()
    phone = models.TextField()


class Rialto(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    definitions = models.TextField()
    presentation = models.FileField()


# class ActionHistory(models.Model):
#     job_seek = models.ForeignKey('JobSeek',on_delete=models.DO_NOTHING, db_column='job_seek')
#     action_name = models.TextField()
#     value_before = models.TextField()
#     value_after = models.TextField()
#     data = models.DateField()
#     comment = models.TextField(null=True)
#
#     class Meta:
#         db_table = 'actionHistory'
#         verbose_name = 'ActionHistory'
#         verbose_name_plural = 'ActionHistory'
