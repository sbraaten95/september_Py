from django.shortcuts import render, HttpResponse, redirect
from django.conf.urls.static import static

def index(request):
	return render(request, 'disappearing_ninja_app/index.html')
def show_all(request):
	context = {
		"color": 'all'
	}
	return render(request,'disappearing_ninja_app/ninjas.html', context)
def ninja_color(request, color):
	context = {
	"color": color
	}
	return render(request,'disappearing_ninja_app/ninjas.html', context)