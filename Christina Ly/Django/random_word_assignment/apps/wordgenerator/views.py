from django.shortcuts import render, redirect
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
		return redirect('/')
	else:
		return redirect('/')
def reset(request):
	request.session['count']=0
	request.session['word'] = ""
	return redirect('/')