from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserLoginForm
from django.contrib import messages

from django.contrib.auth import login, authenticate, logout

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        creation_form =  UserCreationForm(request.POST)

        if creation_form.is_valid():
            creation_form.save()

            name = request.POST.get('name')
            messages.success(request, f"Account is created for {name}")
            return redirect('register')
        else:
            messages.warning(request, f'Please Correct the errors!{str(creation_form.errors)}')

    creation_form = UserCreationForm()
    login_form = UserLoginForm()
    context = {
        'creation_form':creation_form,
        'login_form':login_form,
    }
    return  render(request, 'register.html', context)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.name.title()}! You are logged in now.")
            return redirect('home')
        else:
            messages.warning(request, 'Username OR Password is incorrect!')
            return redirect('register')

    return redirect('home')


def logout_view(request):
    messages.success(request, f" Thanks {request.user.name.title()} for using our Application. We are happy with you, Please come again.")
    logout(request)
    return redirect('register')