from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	# users = User.objects.all()
	# for user in users:
	# 	print user.email
	# 	print user.password

	if not 'errors' in request.session:
		request.session['errors'] = []
	return render(request, 'first_app/index.html')

def register(request):
	result = User.objects.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['conf_password'])
	if result[0]:
		request.session['email'] = result[1].email
		request.session['first_name'] = request.POST['first_name']
		request.session.pop('errors')
		return redirect('/success')
	else:
		request.session['errors'] = result[1]
		return redirect('/')

def login(request):
	login_result = User.objects.login(request.POST['email'], request.POST['password'])
	print login_result
	if login_result[0]:
		request.session['email'] = login_result[1].email
		request.session['first_name'] = login_result[1].first_name
		request.session.pop('login_errors')
		return redirect('/success')
	else:
		request.session['login_errors'] = login_result[1]
		return redirect('/')

	return render(request, 'first_app/success.html')

def success(request):
	result = User.objects.all()
	return render(request, 'first_app/success.html')
