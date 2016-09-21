import time
from django.shortcuts import render

# Create your views here.
def index(request):
	currtime = {
		"line1": time.strftime("%B %d, %Y"),
		"line2": time.strftime("%I:%M %p")
	}
	return render(request, 'timedisplay/index.html', currtime)