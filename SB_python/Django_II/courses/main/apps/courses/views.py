from django.shortcuts import render, redirect
from .models import Course
from ..loginreg.models import User

# Create your views here.
def index(request):
	context = {
		'courses' : Course.objects.all(),
		'users' : User.objects.all()
	}

	for e in context['courses']:
		Course.objects.filter(id=e.id) | Course.objects.filter(cour)

	return render(request, 'courses/index.html', context)

def add(request):
	Course.objects.create(name = request.POST['name'], description = request.POST['description'], course_taker = request.POST['user'])
	return redirect('/')

def commence(request, id):
	context = {
		"course" : Course.objects.get(id=id)
	}
	return render(request, 'courses/destroy.html', context)

def complete(request, id):
	Course.objects.get(id=id).delete()
	return redirect('/')