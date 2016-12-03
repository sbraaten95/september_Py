from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'survey/index.html')

def process(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1
	request.session['data'] = {'name': request.POST['name'], 'location': request.POST['location'], 'lang': request.POST['lang'], 'comm': request.POST['comm']}
	request.session['name'] = request.POST['name']
	return redirect('/result')

def result(request):
	return render(request, 'survey/result.html')

def back(request):
	return redirect('/')