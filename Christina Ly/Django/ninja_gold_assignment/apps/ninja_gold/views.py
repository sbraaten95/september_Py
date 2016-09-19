from django.shortcuts import render, redirect, HttpResponse
import random
import datetime

def index(request):
	try:
		if request.session['gold']:
			print request.session['gold']
	except:
		request.session['gold'] = 0
		request.session['activites'] = ''
	return render(request,'ninja_gold/index.html')
def process(request):
	date = datetime.datetime.now().strftime('(%Y-%m-%d %I:%M %p)')
	if request.POST['building'] == 'farm':
		earn = random.randrange(10,21)
		request.session['gold'] += earn
		request.session['activities'] ='Earned ' +str(earn)+' golds from the farm ' +str(date)+'<br>' + request.session['activities']
	elif request.POST['building'] == 'cave':
		earn = random.randrange(5,11)
		request.session['gold'] += earn
		request.session['activities'] = 'Earned ' +str(earn)+' golds from the cave ' +str(date)+'<br>'	+ request.session['activities']
	elif request.POST['building'] == 'house':
		earn = random.randrange(2,6)
		request.session['gold'] += earn
		request.session['activities'] = 'Earned ' +str(earn)+' golds from the house ' +str(date)+'<br>'+ request.session['activities']
	elif request.POST['building'] == 'casino':
		earn = random.randrange(-50,51)
		if earn < 0:
			request.session['gold'] += earn
			request.session['activities'] = 'Entered a casino and lost ' +str(earn)+' golds... Ouch.. ' +str(date)+'<br>'+ request.session['activities']
		if earn > 0:
			request.session['gold'] += earn
			request.session['activities'] = 'Entered a casino and won ' +str(earn)+' golds ' +str(date)+'<br>'+ request.session['activities']
	return redirect('/')
def reset(request):
	request.session['gold'] = 0
	request.session['activities'] = ''
	return redirect('/')