from django.shortcuts import render, redirect
from .models import User
import bcrypt

def index(request):
	try:
		request.session['message']
	except:
		request.session['message'] = ''
	return render(request, 'login_registration/index.html')
def register(request):
	email_validate = User.objects.validate(request.POST['email'])
	info_validate = User.objects.register(request.POST['first_name'],request.POST['last_name'],request.POST['password'], request.POST['confirm']) 
	password = request.POST['password']
	if email_validate and info_validate:
		request.session['first_name'] = request.POST['first_name']
		request.session['regorlogin'] = 'registered'
		password = password.encode('utf-8')
		hashed = bcrypt.hashpw(password, bcrypt.gensalt())
		first_name = request.POST['first_name'];
		last_name = request.POST['last_name'];
		email = request.POST['email'];
		User.objects.create(email = email, first_name = first_name, last_name = last_name, password = hashed)
		return redirect('/success')
	elif not email_validate:
		request.session['message'] = "Email is not valid"
	elif not info_validate:
		request.session['message'] = "First Name required and must letters\r\n Last Name required and must have letters \r\n Password Required with no fewer than 8 characters and must match passwowrd confirmation"
	return redirect('/')
def login(request):
	login_validate = User.objects.login_valid(request.POST['email'], request.POST['password'])
	if login_validate:
		request.session['message'] = ''
		request.session['first_name'] = User.objects.get(email =request.POST['email']).first_name
		request.session['regorlogin'] = 'logged in!'
		return redirect('/success')
	elif not login_validate:
		request.session['message']= 'Wrong login credentials'
	return redirect('/')
def success(request):
	return render(request, 'login_registration/success.html')