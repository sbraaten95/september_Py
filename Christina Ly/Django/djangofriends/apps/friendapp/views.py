from django.shortcuts import render, redirect, HttpResponse
from . models import Users, Friendships

def index(request): 
	users = Users.objects.get(id = 1)
	context = {'users': [users]}
	return render(request, "friendapp/index.html", context)
	##users must be wrapped in an array for the get function to work

def filterlast(request):
	users = Users.objects.filter(last_name = "Rodriguez")	
	context = {'users': users}
	return render(request, "friendapp/index.html", context)

def excludelast(request):
	users = Users.objects.exclude(last_name = "Rodriguez")
	context = {'users': users}
	return render(request, "friendapp/index.html", context)

def chaining(request):
	users = Users.objects.filter(last_name = "Rodriguez") | Users.objects.filter(first_name ="Daniel")
	context = {'users': users}
	return render(request, "friendapp/index.html", context) 

def madison(request):
	users = Users.objects.filter(last_name = "Rodriguez").exclude(first_name = "Madison")
	context = {'users': users} 
	return render(request, "friendapp/index.html", context)	

def danmike(request):
	users = Users.objects.exclude(first_name ="Daniel").exclude(first_name = "Michael")
	context = {'users': users}
	return render(request, "friendapp/index.html", context)

def getrodriguez(request):
	users = Users.objects.get(last_name = "Rodriguez")
	print users
	context = {'users': users}
	return render(request, "friendapp/index.html", context)
	#### errors will occur for get function if more than one result

def getthousand(request):
	users = Users.objects.get(id = 10000)
	context = {'users': users}
	return render(request, "friendapp/index.html", context)
	#### errors will occur because query matching does not exist

def orderfirst(request):
	users = Users.objects.all().order_by('first_name')
	context = {'users': users}
	return render(request, "friendapp/index.html", context)

def orderreverse(request):
	users = Users.objects.all().order_by('last_name').reverse()
	context = {'users': users}
	return render(request, "friendapp/index.html", context)

def all(request):
	allusers = Users.objects.all()
	print allusers 

def friendship4table(request):
	friendships = Friendships.objects.filter(user = 4)
	## all ppl with friendships with user id = 4
	for friendship_object in friendships:
		print friendship_object.friend.first_name
	return render(request, "friendapp/index.html")
	########only the friends' firstname of user = 4  displayed in the terminal

def frienduser4(request):
	friendships = Friendships.objects.filter(friend = 4)
	print friendships
	return render (request, "friendapp/index.html")

def friendnot(request):
	users = Friendships.objects.exclude(user = 4).exclude(user = 5).exclude(user = 6)
	for friendship_object in users:
		print friendship_object.user.id
	return render(request, "friendapp/index.html")