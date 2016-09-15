from django.shortcuts import render,HttpResponseRedirect,redirect,Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from KYusers.models import *
def context_call(request):
    context = {
        'user': request.user,
    }
    return context

def IndexView(request):
    template_name = 'index.html'
    return render(request,template_name,{})

def RegisterView(request,template_name):
    post = request.POST
    context = {
        'all_colleges':College.objects.all(),
    }
    email = post.get('email')
    form = RegisterForm(request.POST)
    print form.is_valid()
    user,created = User.objects.get_or_create(username=email,email=email)
    if created:
        # print 'USER CREATED'
        user.first_name = post.get('name')
        password = post.get('password')
        user.set_password(password)
        user.save()
        # print 'USER SAVED'
        kyprofile = KYProfile(user=user)
        kyprofile.sex = post.get('sex')
        kyprofile.year = post.get('year')
        kyprofile.mobile_number = post.get('mobile_number')
        # print 'COLEGE GETING OR CREATING'
        college,created = College.objects.get_or_create(collegeName=post.get('college'))
        kyprofile.college = college
        kyprofile.save()
        # print 'KYPROFILE SAVED'

        new_user = authenticate(username=email, password=password)
        login(request, new_user)
        # print 'USER LOGGED IN'
        return redirect('/dashboard')
    else:#allready a user
        messages.warning(request,'email allready registered!',fail_silently=True)
        return render(request,template_name,context)


def LoginView(request,template_name,context):
    post = request.POST
    email = post.get('email')
    password = post.get('password')
    form = LoginForm(request.POST)
    print form.is_valid()
    user = authenticate(username=email, email=email, password=password)
    print user
    if user is not None:
        login(request, user)
        print 'logging In'
        return redirect('/dashboard')
    else:
        messages.error(request,'Invalid Credentials',fail_silently=True)
        return render(request,template_name,context)


def FormView(request):
    context = {
    "regform" : RegisterForm(),
    "logform" : LoginForm(),
    "all_colleges" : College.objects.all(),
    }
    template_name = 'form.html'
    if request.method == "POST":
        if "register" in request.POST:
            return RegisterView(request,template_name,context)
        elif "login" in request.POST:
            return LoginView(request,template_name,context)
    else:
        return render(request,template_name,context)

def CARegistrationsView(request):
    if request.method == 'POST':
        post = request.POST
        caprofile = CAProfile.objects.create(kyprofile=request.user.kyprofile)
        caprofile.collegeAddress = post.get('collegeAddress')
        caprofile.postalAddress = post.get('postalAddress')
        caprofile.pincode = post.get('pincode')
        request.user.kyprofile.is_ca = True
        request.user.kyprofile.save()
        caprofile.save()
        
    else:
        pass

@login_required(login_url='/login')
def DashboardView(request):
    template_name = 'dashboard.html'
    context = context_call(request)
    return render(request,template_name,context)

@login_required(login_url='/login')
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')
