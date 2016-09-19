from django.shortcuts import render, HttpResponse
from .models import User

def index(request):
	User.objects.login('sperios@codingdojo.com', "Speros")
	return HttpResponse (User.objects.login('sperios@codingdojo.com', "Speros"))