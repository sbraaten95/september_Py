from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt

# Create your models here.

class UserManager(models.Manager):
	def register(self, request):
		errors = {}

		if len(request.POST['name']) < 2:
			errors['nameshort'] = "Name is too short!"
		for s in request.POST['name']:
			if not s.isalpha():
				errors['namenotalpha'] = "Name can only be letters!"

		if len(request.POST['alias']) < 6:
			errors['alias'] = "Alias is too short!"

		try:
			validate_email(request.POST['email'])
		except ValidationError:
			errors['email'] = "Invalid email!"

		if len(request.POST['password']) < 8:
			errors['password'] = "Password too short!"

		if request.POST['password'] != request.POST['dblcheck']:
			errors['dblcheck'] = "Passwords do not match!"

		return errors

	def login(self, request):
		errors ={}

		try:
			user = User.objects.get(email=request.POST['email'])
			password = request.POST['password'].encode()
			print user.password
			if not bcrypt.hashpw(password, user.password.encode()):
				errors['wrong'] = "Email/password don't match."

		except ObjectDoesNotExist:
			errors['wrong'] = "Email/password don't match."

		return errors


class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=100)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	objects = UserManager()