from django.contrib.auth.models import User
from django import forms
from KYusers.models import *

class RegisterForm(forms.ModelForm):

    name = forms.CharField(label="Name",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','placeholder':'Name',}))

    sex = forms.ChoiceField(widget=forms.Select(attrs={'class': 'sex','required':'true', 'placeholder':'Sex', }),choices=sex_choices,)

    year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'year', 'required':'true','placeholder':'Year', }),choices=year_choices,)

    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Email'}))

    password = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'password', 'placeholder':'Password', 'name': 'password'}))

    college = forms.CharField(label="College",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'text', 'placeholder':"College"}))

    mobile_number = forms.IntegerField(label="Mobile Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'number', 'placeholder':"Mobile Number"}))


    class Meta:
        model = KYProfile
        fields = ['name','email','password','year','sex','college','mobile_number']
        exclude = ['user_id','user','profile_photo']



class LoginForm(forms.Form):
    email = forms.CharField(label="email",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email','required':'true', 'type':'text','name': 'email'}))
    password = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Password','required':'true', 'type':'password','name': 'password'}))
