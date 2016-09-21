from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'survey/index.html')
def process_users(request):
	print (request.method)
	request.session['context']= {
	'name': request.POST['name'],
	'location': request.POST['location'],
	'language': request.POST['language'],
	'comments': request.POST['comments']
	}
	if request.method == "POST":
		try:
			request.session['count'] += 1
		except:
			request.session['count'] = 1
		print(request.POST)
		return redirect(reverse('survey:my_result'))
	else:
		return redirect(reverse('survey:my_index'))
def result_users(request):
	return render(request, 'survey/users.html', request.session['context'])
def reset(request):
	request.session['count']=0
	request.session['context'] = ""
	return redirect(reverse('survey:my_index'))