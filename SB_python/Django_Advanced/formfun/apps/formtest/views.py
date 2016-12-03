from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.
def index(request):
	form = RegistrationForm()
	context = {
		"myregistrationform" : form
	}
	return render(request, 'formtest/index.html', context)