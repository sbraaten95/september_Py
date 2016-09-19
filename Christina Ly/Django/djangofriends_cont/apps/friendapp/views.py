from django.shortcuts import render, redirect, HttpResponse
from . models import Users, Friendships

def one(request): 
	friendship_objects = Friendships.objects.all()
	context = {'friendships': friendship_objects}
	return render(request, "friendapp/index.html", context)
	
def two(request):
	friendship_objects = Friendships.objects.filter(user__first_name = "Michael")
	context ={'friendships': friendship_objects}
	return render(request, "friendapp/index.html", context)

def three(request):
	friendship_objects = Friendships.objects.exclude(friend__first_name = "Daniel")
	context ={'friendships': friendship_objects}
	return render(request, "friendapp/index.html", context)

def four(request):
	friendship_objects = Friendships.objects.filter(user__id = 1, user__last_name = 'Hernandez')
	context ={'friendships': friendship_objects}
	return render(request, "friendapp/friends.html", context)
	#### found friends who each are friends with BOTH user id = 1 and hernandez
	#### to find those who each friends with either id = 1 and hernandez use "|"

def five(request):
	friendship_objects = Friendships.objects.filter(user__id = 1)| Friendships.objects.filter(user__last_name = 'Hernandez').order_by('friend__first_name')
	context ={'friendships': friendship_objects}
	return render(request, "friendapp/friends.html", context)

def six(request):
	users = Users.objects.filter(usersfriend__friend__id=2)
	print (users.query)
	## was able to grab the related name

def seven(request):
	users = Users.objects.filter(usersfriend__friend__id=2)
	print users
	context = {'users': users}
	return render(request, "friendapp/users.html", context)

def eight(request):
	users = Users.objects.filter(friendsfriend__user__id=1).distinct()|Users.objects.filter(friendsfriend__user__last_name = "Hernandez").distinct()
	context = {'users': users}
	return render(request, "friendapp/users.html", context)
