from django.shortcuts import render
from .models import User
def index(request):
	print(User.objects.all())
	User.objects.create(first_name = "Minahm", last_name="Kim", password = "1234asdf")
