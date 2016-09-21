from django.shortcuts import render, redirect
from time import strftime, localtime
import random

# Create your views here.
def index(request):
	if 'wallet' not in request.session:
		request.session['wallet'] = 0
	if 'activity_log' not in request.session:
		request.session['activity_log'] = ''
	return render(request, 'gold/index.html')

def process_money(request):
	if request.method == 'POST':
		time = strftime("(%Y/%m/%d %I:%M %p)", localtime())
		if request.POST['building'] == 'farm':
			roll = int(random.randrange(10,21))
			request.session['activity_log'] += '<span class="green">Earned '+str(roll)+ ' golds from the farm! '+time+'</span><br>'
			request.session['wallet'] += roll
		elif request.POST['building'] == 'cave':
			roll = int(random.randrange(5,11))
			request.session['activity_log'] += '<span class="green">Earned '+str(roll)+ ' golds from the cave! '+time+'</span><br>'
			request.session['wallet'] += roll
		elif request.POST['building'] == 'house':
			roll = int(random.randrange(2,6))
			request.session['activity_log'] += '<span class="green">Earned '+str(roll)+ ' golds from the house! '+time+'</span><br>'
			request.session['wallet'] += roll
		elif request.POST['building'] == 'casino':
			roll = int(random.randrange(0,51))
			win = int(random.randrange(0,2))
			if win:
				request.session['activity_log'] += '<span class="green">Entered a casino and earned '+str(roll)+ ' golds! '+time+'</span><br>'
			else:
				request.session['activity_log'] += '<span class="red">Entered a casino and lost '+str(roll)+ ' golds... Ouch.. '+time+'</span><br>'
				roll *= -1
			request.session['wallet'] += roll
	return redirect('/')