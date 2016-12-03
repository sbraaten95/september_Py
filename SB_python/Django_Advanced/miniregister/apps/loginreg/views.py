from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
	return render(request, 'loginreg/index.html')

def register(request):
	form = RegisterForm()

	if request.methods == 'POST':
		input_form = RegisterForm(request.POST)

		if input_form.is_valid():
			request.session['user'] = request.POST['email']
			context = {
				'user' : User.objects.get(email=request.session['user'])
			}
			return render(request, 'loginreg/success.html', context)
		else:
			return render(request, 'loginreg/index.html', input_form.errors)