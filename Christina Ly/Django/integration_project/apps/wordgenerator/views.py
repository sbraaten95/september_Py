from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
import random, string

def index(request):
	return render(request,'wordgenerator/index.html')
def create(request):
	if request.method =="POST":
		try:
			request.session['count'] += 1
		except:
			request.session['count'] = 1
		request.session['word'] = "".join([random.choice(string.ascii_uppercase +string.digits) for n in xrange(14)])
		print (request.POST)
		return redirect(reverse('word:my_index'))
	else:
		return redirect(reverse('word:my_index'))
def reset(request):
	request.session['count']=0
	request.session['word'] = ""
	return redirect(reverse('word:my_index'))