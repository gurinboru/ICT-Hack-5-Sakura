from django.contrib import admin
from .models import Organization,Student,Project,StudentProject,Rialto

admin.site.register(Organization)
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(StudentProject)
admin.site.register(Rialto)