from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from ..courses.models import Course
from ..loginreg.models import User
from .models import Merge


# Create your views here.
def index(request):
	numbers = Merge.objects.values("course").annotate(num_users=Count('user')).order_by('course_id')
	context = {
		'courses' : Course.objects.all(),
		'users' : User.objects.all(),
		'number_users' : numbers
	}
	return render(request, 'integration/index.html', context)

def merge(request):
	Merge.objects.create(course = Course.objects.get(id=request.POST['course']), user = User.objects.get(id=request.POST['user']))
	return redirect(reverse('integration:integration_index'))