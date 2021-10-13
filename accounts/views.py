# Create your views here.
import re
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm 
from django.views.decorators.csrf import csrf_exempt


app_name= 'accounts'

@csrf_exempt
def sign_up(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('index')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/sign_up.html", context={"register_form":form, "sign":True})

@csrf_exempt
def login_try(request):
	if request.method == "POST":
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('index')
			else:
				messages.error(request,"Invalid username or password.")
				print("Use None")


		else:
			messages.error(request,"Invalid username or password.")
			print("Not vaild")
	else:
		print("Not Post")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form, "sign":True})

def logout(request):
	auth.logout(request)
	return redirect('index')	