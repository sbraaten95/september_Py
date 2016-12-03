from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 100
	return render(request, 'ninjagold/index.html')

def process(request, choice):
	if 'activities' in request.session:
		request.session['activities'].reverse()
	result = ''
	if choice == 'farm':
		coin = random.randrange(10, 21)
		request.session['gold'] += coin
		if coin > 0:
			result = 'You earned ' + str(coin) + ' gold! (' + str(datetime.date.today()) + ' ' + str(datetime.datetime.now()) + ')'
		else:
			result = 'You lost ' + str(coin) + ' gold! (' + str(datetime.date.today()) + ' ' + str(datetime.datetime.now()) + ')'
	elif choice == 'cave':
		coin = random.randrange(-10, 10)
		request.session['gold'] += coin
		if coin > 0:
			result = 'You earned ' + str(coin) + ' gold! (' + str(datetime.date.today()) + ' ' + str(datetime.datetime.now()) + ')'
		else:
			result = 'You lost ' + str(coin) + ' gold! (' + str(datetime.date.today()) + ' ' + str(datetime.datetime.now()) + ')'
	if choice == 'house':
		coin = random.randrange(-5, 5)
		request.session['gold'] += coin
		if coin > 0:
			result = 'You earned ' + str(coin) + ' gold! (' + str(datetime.date.today()) + ' ' + str(datetime.datetime.now()) + ')'
		else:
			result = 'You lost ' + str(coin) + ' gold! (' + str(datetime.date.today()) + ' ' + str(datetime.datetime.now()) + ')'
	if choice == 'casino':
		coin = random.randrange(-500, 400)
		request.session['gold'] += coin
		if coin > 0:
			result = 'You earned ' + str(coin) + ' gold! (' + str(datetime.date.today()) + ' ' + str(datetime.datetime.now()) + ')'
		else:
			result = 'You lost ' + str(coin) + ' gold! (' + str(datetime.date.today()) + ' ' + str(datetime.datetime.now()) + ')'

	if 'activities' in request.session:
		request.session['activities'].append(result)
		request.session['activities'].reverse()
	else:
		request.session['activities'] = []
	return redirect('/')