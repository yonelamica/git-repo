from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

def LoginView(request): 
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username = username, password = pass1)
        if user is not None:
            login(request, user)
            # Login successful!
            messages.success(request, 'Login successful!')
        
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request, 'users/login.html')

def LogoutView(request):
    logout(request)
    return redirect('login')

def webpage1(request):
    return render(request, 'users/page1.html')

def webpage2(request):
    return render(request, 'users/page2.html')


@login_required()
def profile(request):
    return render(request, 'users/profile.html')