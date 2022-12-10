from django import forms
from django.forms import NumberInput


class changeForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"ФИО"}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"89........."}),required=True)
    phone = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"example@mail.ru"}),required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Муж/жен"}),required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Разработчик"}),required=True)
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "placeholder":"Фото"}),required=False)
    tags = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class":"form-control", "placeholder":"01.01.1999"}),required=True)
    CV = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    education = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    department = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    hardskill_softskill = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)
    experience = forms.DateField(widget=NumberInput(attrs={'type': 'date', "class": "form-control", "placeholder": "01.01.1999"}),
                       required=True)