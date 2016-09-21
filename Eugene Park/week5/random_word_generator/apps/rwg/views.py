from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
	if 'counter' not in request.session:
		request.session['counter'] = 0
	request.session['counter'] += 1
	word_set = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
	word = ''
	for x in range(1,15):
		rand = random.randint(0,35)
		word += word_set[rand]
	request.session['word'] = word
	return render(request, 'rwg/index.html')

def generate(request):
	return redirect('/')