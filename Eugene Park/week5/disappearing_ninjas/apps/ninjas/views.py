from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'ninjas/index.html')
def all_ninjas(request):
	context = {'color': "all_ninja.css"}
	return render(request, 'ninjas/ninjas.html', context)
def ninja(request, ninja_color):
	if ninja_color == 'blue':
		context = {'color': "blue.css"}
	elif ninja_color == 'orange':
		context = {'color': "orange.css"}
	elif ninja_color == 'red':
		context = {'color': "red.css"}
	elif ninja_color == 'purple':
		context = {'color': "purple.css"}
	else:
		context = {'color': "megan.css"}
	return render(request, 'ninjas/ninjas.html', context)