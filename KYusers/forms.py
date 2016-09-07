from django.contrib.auth.models import User
from django import forms
from KYusers.models import KYProfile, year_choices

class RegisterForm(forms.ModelForm):

    first_name = forms.CharField(label="First Name",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First Name',}))

    last_name = forms.CharField(label="Last Name",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last Name',}))

    year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Year', }),choices=year_choices,)

    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Email'}))

    password = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','required':'true','type':'password', 'placeholder':'Password', 'name': 'password'}))

    college = forms.CharField(label="College",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'text', 'placeholder':"College"}))

    mobile_number = forms.IntegerField(label="Mobile Number",
                               widget=forms.TextInput(attrs={'class': 'form-control','type':'number', 'placeholder':"Mobile Number"}))


    class Meta:
        model = KYProfile
        fields = ['first_name', 'last_name','email','password','year','college','mobile_number']
        exclude = ['user_id','user','profile_photo']



class LoginForm(forms.Form):
    email = forms.CharField(label="email",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Email','required':'true', 'type':'text','name': 'email'}))
    password = forms.CharField(label="Password",
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Password','required':'true', 'type':'password','name': 'password'}))
