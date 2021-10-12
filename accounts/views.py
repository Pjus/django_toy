# Create your views here.
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

app_name= 'accounts'

def sign_up(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request, "accounts/sign_up.html", context={"register_form":form})

def login_try(request):
	status = "logout"
	if request.user.is_authenticated:
		status = "login"
	return render(request, 'accounts/login.html', {'status':status})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
    return render(request,'login.html')