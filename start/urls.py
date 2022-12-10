from django.urls import path
from start import views

urlpatterns = [
    path('', views.start),
    path('students', views.students),
    path('curstudent/<int:pk>', views.getStudent, name='curstudent'),
]