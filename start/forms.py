from django import forms
from django.forms import NumberInput
from .models import ContactPerson


class changeStudentForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Имя..."}),required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Фамилия..."}),required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Телефон..."}),required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"Email..."}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "placeholder":"Фото..."}),required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={ "class":"form-control", "placeholder":"Теги..."}),required=False)
    CV = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    education = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Образование..."}),
                       required=False)
    department = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Факультет..."}),
                       required=False)
    hardskill_softskill = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Навыки..."}),
                       required=False)
    experience = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Опыт..."}),
                       required=False)
    ISU = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "ИСУ..."}),
                                  required=False)

class addProjectForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Название..."}),
                       required=True)
    definitions = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Описание..."}),
                       required=True)
    budjet = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control1", "placeholder": "Бюджет..."}),
                       required=True)
    dedlines = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control1", "placeholder": "Сроки..."}),
                       required=True)
    positions = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Должности..."}),
                       required=True)
    techDocument = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "ТЗ..."}),
                       required=True)
    goalOfProject = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Цель..."}),
                       required=True)
    background = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Опыт..."}),
                       required=True)
    result = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Результат..."}),
                       required=True)
    criterias = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Критерии..."}),
                       required=True)
    tags = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Теги..."}),
                       required=False)
    contactPersonName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ФИО..."}),
                       required=True)
    contactPersonPhone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Телефон..."}),
                       required=True)
    contactPersonEmail = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email..."}),
                             required=True)


class changeOrganizationForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email..."}),
                             required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Контактное лицо..."}),
                               required=True)

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Название..."}),
                               required=True)
    INN = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "ИНН..."}),
                               required=True)

class addRialtoForms(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя..."}),
                               required=True)
    definitions = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Описание..."}),
                               required=True)
    presentation = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": ""}),
                       required=True)
    investment = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Инвестиции..."}),
                       required=True)
    dedline = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control", "placeholder": "Сроки..."}),
                       required=True)
    FCF = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "FCF..."}),
                       required=True)