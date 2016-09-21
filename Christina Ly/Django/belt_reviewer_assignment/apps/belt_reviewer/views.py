from django.shortcuts import render, redirect
from .models import Book, Review
from django.core.urlresolvers import reverse
from ..login_registration.models import User


def index(request):
	context={
		'user': User.objects.get(id=request.session['id']),
		'books':Book.objects.all(),
		'reviews': Review.objects.all()
	}
	return render(request, 'belt_reviewer/index.html', context)
def add(request):
	context={
		"books": Book.objects.all()
	}
	return render(request, 'belt_reviewer/add.html', context)
def create(request):
	user = User.objects.get(id =request.session['id'])
	if len(request.POST['author_text']) ==0:
		book=Book.objects.create(name = request.POST['title'], author = request.POST['author_select'])
		review = Review.objects.create(book = book, user = user, rating = request.POST['stars'], review = request.POST['review'])
	else:
		book = Book.objects.create(name = request.POST['title'], author = request.POST['author_text'])
		review = Review.objects.create(book = book, user = user, rating = request.POST['stars'], review = request.POST['review'])
	return redirect(reverse('belt:books_home'))
def detail(request, id):
	context={
		'book': Book.objects.get(id = id),
		'reviews': Review.objects.filter(book__id = id)
 	}
	return render(request, 'belt_reviewer/detail.html', context)
def delete(request, id):
	book_id = Review.objects.get(id =id).book.id
	review = Review.objects.get(id = id).delete()
	return redirect(reverse('belt:detail', kwargs={'id':book_id}))
def update(request, id):
	user = User.objects.get(id =request.session['id'])
	book = Book.objects.get(id=id)
	review = Review.objects.create(book = book, user = user, rating = request.POST['stars'], review = request.POST['review'])
	return redirect(reverse('belt:detail', kwargs={'id':id}))