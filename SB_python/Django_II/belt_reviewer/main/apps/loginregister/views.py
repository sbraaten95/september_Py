from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
from ..reviews.models import Book, Review
import bcrypt

# Create your views here.
def index(request):
	return render(request, 'loginregister/index.html')

def register(request):
	errors = User.objects.register(request)

	if len(errors) > 0:
		context = {
			'errors' : errors
		}
		return render(request, 'loginregister/index.html', context)

	else:
		password = request.POST['password'].encode()
		newpass = bcrypt.hashpw(password, bcrypt.gensalt())
		User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=newpass)
		request.session['user'] = User.objects.get(email=request.POST['email']).email
		context = {
			'user': User.objects.get(email=request.POST['email']),
			'books': Book.objects.all(),
			'reviews': Review.objects.all()
		}
		return render(request, 'reviews/books.html', context)

def login(request):
	errors = User.objects.login(request)

	if len(errors) > 0:
		context = {
			'errors' : errors
		}
		return render(request, 'loginregister/index.html', context)

	else:
		request.session['user'] = request.POST['email']
		context = {
			'user' : User.objects.get(email=request.POST['email']),
			'books': Book.objects.all(),
			'reviews': Review.objects.all()
		}
		return render(request, 'reviews/books.html', context)

def logoff(request):
	request.session.flush()
	return redirect(reverse('loginreg:index'))