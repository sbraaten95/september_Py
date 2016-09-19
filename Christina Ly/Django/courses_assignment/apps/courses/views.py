from django.shortcuts import render, redirect
from .models import Courses

def index(request):
	context = {
		'courses': Courses.objects.all()
	}
	request.session['id'] = -1
	return render(request, 'courses/index.html', context)

def courses(request):
	if Courses.objects.validatePresence(request.POST):
		print "success"
		Courses.objects.create(name = request.POST['name'], description = request.POST['description'])
	else:
		print "fail"
	return redirect('/')

def destroyconfirm(request, id):
	request.session['id']=id
	context = {
	'course': Courses.objects.get(id = id)
	}
	return render(request, 'courses/destroy.html', context)

def destroy(request):
	Courses.objects.get(id = request.session['id']).delete()
	return redirect('/')

