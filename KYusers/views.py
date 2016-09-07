from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def context_call(request):
    context = {
        'user': request.user,
    }
    return context

def IndexView(request):
    template_name = 'index.html'
    return render(request,template_name,{})

def RegisterView(request):
    template_name = 'register.html'
    if request.method == "POST":
        form = RegisterForm(request.POST)
        post = request.POST
        if form.is_valid:
            email = post['email']
            try:
                allready_a_user = User.objects.get(username=email)
            except:
                allready_a_user = None
            if allready_a_user is None:
                user = User.objects.create_user(username=email, email=email)
                user.first_name = post['first_name']
                user.last_name = post['last_name']
                password = post['password']
                user.set_password(password)
                user.save()

                kyprofile = form.save(commit=False)
                kyprofile.user = user
                kyprofile.save()

                new_user = authenticate(username=email, password=password)
                login(request, new_user)

                return redirect('/dashboard')
            else:#allready_a_user
                messages.warning(request,'email allready registered!',fail_silently=True)
                return render(request,template_name,{'form':form})
        else:
            return render(request,template_name,{'form':form})
    else:
        return render(request,template_name,{'form':RegisterForm()})


def LoginView(request):
    template_name = 'login.html'
    if request.method == "POST":
        post = request.POST
        form = LoginForm(post)

        if form.is_valid:
            email = post['email']
            password = post['password']

            user = authenticate(username=email, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/dashboard')
            else:
                messages.error(request,'Invalid Credentials',fail_silently=True)
                return render(request,template_name,{'form':form})
        else:
            return render(request,template_name,{'form':form})
    else:
        return render(request,template_name,{'form': LoginForm()})


@login_required(login_url='/login')
def DashboardView(request):
    template_name = 'dashboard.html'
    context = context_call(request)
    return render(request,template_name,context)

@login_required(login_url='/login')
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')
