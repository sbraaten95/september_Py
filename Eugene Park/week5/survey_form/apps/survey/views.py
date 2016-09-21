from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'survey/index.html')

def submit_form(request):
	if 'counter' not in request.session:
		request.session['counter'] = 0
	request.session['counter'] += 1
	if request.method == "POST":
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comment'] = request.POST['comment']
	return redirect('/result')

def result(request):
	return render(request, 'survey/result.html')