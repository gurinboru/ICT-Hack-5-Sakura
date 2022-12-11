from django.urls import path
from start import views

urlpatterns = [
    path('', views.start),
    path('students', views.students, name='students'),
    path('projects', views.projects, name='projects'),
    path('curstudent/<int:pk>', views.getStudent, name='curstudent'),
    path('curproject/<int:pk>', views.getProject, name='curproject'),
    path('add_project', views.addProject),
    path('add_rialto', views.addRialto),
    path('profile', views.cangeProfile, name='profile'),
    path('rialtos', views.rialtos, name='rialtos'),
    path('currialto/<int:pk>', views.getRialto, name='currialto'),
    path('curstudent/get_cv/<int:pk>',views.get_cv),
    path('currialto/get_presentation/<int:pk>',views.get_presentation),
    path('myapplications', views.myApplications, name='myapplications'),
]