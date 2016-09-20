from django.shortcuts import render, redirect, HttpResponse
from .models import Email
import re

# Create your views here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
	if not 'errors' in request.session: 
		request.session['errors'] = []
	return render(request, 'first_app/index.html')

def create(request):
	if request.method == "POST":
		result = Email.emailMgr.register(request.POST['email'])
		if result[0]:
			request.session['email'] = result[1].email
			request.session.pop('errors')
			return redirect('/success')
		else:
			request.session['errors'] = result[1]
			return redirect('/')
	else:
		return redirect('/')

def success(request):
	emails = Email.emailMgr.all()
	return render (request, 'emails/success.html')
