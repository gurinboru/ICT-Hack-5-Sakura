from django.urls import path
from start import views

urlpatterns = [
    path('', views.start),
    path('students', views.getStudent),
]