from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from ..loginregister.models import User
from .models import Book, Review

# Create your views here.
def index(request):
	return render(request, 'loginregister/index.html')

def home(request):
	user = User.objects.get(email=request.session['user'])
	context = {
		'user': user,
		'books': Book.objects.all(),
		'reviews': Review.objects.all()
	}
	return render(request, 'reviews/books.html', context)

def add(request):
	context = {
		'reviews': Review.objects.all()
	}
	return render(request, 'reviews/one.html', context)

def submit(request):
	if len(request.POST['newauthor']) > 0:
		author = request.POST['newauthor']
	else:
		author = request.POST['author']

	Book.objects.create(title=request.POST['title'], author=author)

	newbook = Book.objects.get(title=request.POST['title'])

	Review.objects.create(user=User.objects.get(email=request.session['user']), book=newbook, review=request.POST['review'], rating=request.POST['rating'])

	context = {
		'book': newbook,
		'reviews': Review.objects.all()
	}
	return render(request, 'reviews/specific.html', context)

def newreview(request, id):
	Review.objects.create(user=User.objects.get(email=request.session['user']), book=Book.objects.get(id=id), review=request.POST['review'], rating=request.POST['rating'])

	context = {
		'book': Book.objects.get(id=id),
		'reviews': Review.objects.all()
	}
	return render(request, 'reviews/specific.html', context)

def delete(request, id):
	Review.objects.get(book_id = id).delete()
	return redirect(reverse('reviews:home'))

def deletebook(request, id):
	Book.objects.get(id=id).delete()
	return redirect(reverse('reviews:home'))

def showuser(request, id):
	context = {
		'user' : User.objects.get(id=id),
		'reviews' : Review.objects.all(),
		'total' : Review.objects.filter(user__id=id).count()
	}
	return render(request, 'reviews/user.html', context)