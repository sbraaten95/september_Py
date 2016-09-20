from django.shortcuts import render, redirect
from .models import User
import bcrypt

# Create your views here.
def index(request):
	context = {
		'users' : User.objects.all()
	}
	return render(request, 'loginreg/index.html', context)

def login(request):
	email = request.POST['email']
	password = request.POST['password']
	errors = User.objects.login(email, password)
	if len(errors) > 0:
		return render(request, 'loginreg/index.html', errors)
	else:
		context = {
			'user' : User.objects.get(email = email)
		}
		return render(request, 'loginreg/success.html', context)

def register(request):
	firstName = request.POST['first_name']
	lastName = request.POST['last_name']
	email = request.POST['email']
	password = request.POST['password']
	dblCheck = request.POST['dblcheck']
	errors = User.objects.register(firstName, lastName, email, password, dblCheck)
	if len(errors) > 0:
		return render(request, 'loginreg/index.html', errors)
	else:
		password = password.encode()
		realPass = bcrypt.hashpw(password, bcrypt.gensalt())
		User.objects.create(first_name = firstName, last_name = lastName, email = email, password = realPass)
		context = {
			'user' : User.objects.get(email = email)
		}
		return render(request, 'loginreg/success.html', context)

def logoff(request):
	return redirect('/')