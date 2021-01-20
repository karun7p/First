from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
# My forms
from .forms import CreateUserForm 

# Create your views here. 

def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		name = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username= name, password= password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request,'Username or Password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)


def logout_view(request):
	logout(request)
	return redirect('login')


def registration_view(request):
	if request.user.is_authenticated:
		return redirect('home')
		
	form = CreateUserForm(request.POST or None)
	if form.is_valid():
		form.save()
		user = form.cleaned_data.get('username')
		messages.success(request, "Account was created for "+ user)
		return redirect('login')
	else :
		form = CreateUserForm()	
	context = {
		'form': form,
	}
	return render(request, 'accounts/register.html', context)	