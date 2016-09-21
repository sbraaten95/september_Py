from django.shortcuts import render
from .models import User
import bcrypt

# Create your views here.
def index(request):
	return render(request, 'loginregister/index.html')

def register(request):
	name = request.POST['name']
	alias = request.POST['alias']
	email = request.POST['email']
	password = request.POST['password']
	dblcheck = request.POST['dblcheck']
	errors = User.objects.register(name, alias, email, password, dblcheck)
	if len(errors) > 0:
		return render(request, 'loginregister/index.html', errors)
	else:
		password = password.encode()
		newpass = bcrypt.hashpw(password, bcrypt.gensalt())
		User.objects.create(name=name, alias=alias, email=email, password=newpass)
		context = {
			'user': User.objects.get(email=request.POST['email'])
		}
		request.session['id'] = context['user'].id
		return render(request, 'loginregister/books.html', context)

def login(request):
	email = request.POST['email']
	password = request.POST['password']
	errors = User.objects.login(email, password)
	if len(errors) > 0:
		return render(request, 'loginregister/index.html', errors)
	else:
		context = {
			'user' : User.objects.get(email=email)
		}
		request.session['id'] = context['user'].id
		return render(request, 'loginregister/books.html', context)

def add(request):
	return render(request, 'loginregister/add.html')

def home(request):
	return render(request, 'loginregister/home.html')