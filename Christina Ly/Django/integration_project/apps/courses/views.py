from django.shortcuts import render, redirect
from .models import Courses
from django.core.urlresolvers import reverse
from ..login_registration.models import User
from django.db.models import Count

def index(request):
	context = {
		'courses': Courses.objects.all()
	}
	request.session['id'] = -1
	return render(request, 'courses/index.html', context)

def courses(request):
	if Courses.objects.validatePresence(request.POST):
		print "success"
		course = Courses(name = request.POST['name'], description = request.POST['description'])
		course.save()
	else:
		print "fail"
	return redirect(reverse('courses:my_index'))

def destroyconfirm(request, id):
	request.session['id']=id
	context = {
	'course': Courses.objects.get(id = id)
	}
	return render(request, 'courses/destroy.html', context)

def destroy(request):
	Courses.objects.get(id = request.session['id']).delete()
	return redirect(reverse('courses:my_index'))

def integration(request):
	context = {
		'users':User.objects.all(),
		'courses': Courses.objects.annotate(user_count = Count('user')),
	}
	return render(request, 'courses/integration.html', context)
def form(request):
	userid = User.objects.get(id = request.POST.get('user', 1))
	course = Courses.objects.get(id = request.POST.get('course',1))
	course.user.add(userid)
	return redirect(reverse('courses:my_integration'))
