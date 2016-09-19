from django.shortcuts import render, redirect
from .models import Email

def index(request):
	try:
		request.session['message']
	except:
		request.session['message'] = ''
	return render(request, 'email_validation/index.html')

def validate(request):
	email = Email.objects.validate(request.POST['email'])
	if email:
		Email.objects.create(email = request.POST['email'])
		request.session['message'] = ''
		request.session['email'] = request.POST['email']
		return redirect('/success')
	else:
		request.session['message'] = "Email is not valid!"
	return redirect('/')
def success(request):
	emails = Email.objects.all().order_by('-created_at')
	context = {
		'emails': emails
	}
	return render(request, 'email_validation/success.html', context)

