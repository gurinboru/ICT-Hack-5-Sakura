from django.urls import path
from start import views

urlpatterns = [
    path('', views.start),
    path('students', views.students, name='students'),
    path('curstudent/<int:pk>', views.getStudent, name='curstudent'),
    path('profile', views.cangeProfile, name='profile'),
]