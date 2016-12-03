from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AddNote
from .models import Note
import unirest
import re
# Create your views here.

def index(request):
	addform = AddNote()
	context = {
		'addform' : addform,
		'notes' : Note.objects.all()
	}
	return render(request, 'noteapp/index.html', context)

def addNote(request):
	addform = AddNote(request.POST)
	if addform.is_valid():
		addform.save(commit=False)
		addform.save()
	return redirect(reverse('index'))

def getData(request):
	response = unirest.get("https://nutritionix-api.p.mashape.com/v1_1/search/ribeye%2Csteak?fields=item_name%2Citem_id%2Cbrand_name%2Cnf_calories%2Cnf_protein",
		headers={
		"X-Mashape-Key": "5P8MDOP5irmshHGpT0xH3s2UktVXp1zv2JEjsnpTCinqE6xXj2",
		"Accept": "application/json"
		}
	)
	content = response.body

	context = {
		'content' : content['hits'][5]['fields']
	}
	return render(request, 'noteapp/index.html', context)