from django.urls import path
from start import views

urlpatterns = [
    path('', views.start),
    path('students', views.students, name='students'),
    path('projects', views.projects, name='projects'),
    path('curstudent/<int:pk>', views.getStudent, name='curstudent'),
    path('curproject/<int:pk>', views.getProject, name='curproject'),
    path('add_project', views.addProject),
    path('profile', views.cangeProfile, name='profile'),
]