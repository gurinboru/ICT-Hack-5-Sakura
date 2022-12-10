from django import forms
from django.forms import NumberInput
from .models import ContactPerson


class changeStudentForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Имя"}),required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Фамилия"}),required=False)
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"8........"}),required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"Email"}),required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "placeholder":"Фото"}),required=False)
    tags = forms.CharField(widget=forms.TextInput(attrs={ "class":"form-control", "placeholder":"Tags"}),required=False)
    CV = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    education = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Education"}),
                       required=False)
    department = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Department"}),
                       required=False)
    hardskill_softskill = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Skills"}),
                       required=False)
    experience = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Exp"}),
                       required=False)

class addProjectForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    definitions = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    budjet = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    dedlines = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    positions = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    techDocument = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    goalOfProject = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    background = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    result = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    criterias = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    tags = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=False)
    contactPersonName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    contactPersonPhone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    contactPersonEmail = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Муж/жен"}),
                             required=True)


class changeOrganizationForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
                             required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Contact people"}),
                               required=True)

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
                               required=True)
    INN = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "INN"}),
                               required=True)

class addRialto(forms.Form):
    definitions = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Contact people"}),
                               required=True)
    presentation = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)