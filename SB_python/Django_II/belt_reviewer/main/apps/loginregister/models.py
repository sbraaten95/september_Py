from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class UserManager(models.Manager):
	def register(self, name, alias, email, password, dblcheck):
		errors = {}

		if len(name) < 2:
			errors['nameshort'] = "Name is too short!"
		for s in name:
			if not s.isalpha():
				errors['namenotalpha'] = "Name can only be letters!"

		if len(alias) < 6:
			errors['alias'] = "Alias is too short!"

		try:
			validate_email(email)
		except ValidationError:
			errors['email'] = "Invalid email!"

		if len(password) < 8:
			errors['password'] = "Password too short!"

		if password != dblcheck:
			errors['dblcheck'] = "Passwords do not match!"
			
		return errors
	def login(self, email, password):
		errors = {}
		usercheck = User.objects.filter(email=email)
		if len(usercheck) == 0:
			errors['email'] = "Email not found!"
		password = password.encode()
		if not bcrypt.hashpw(password, usercheck.password.encode()):
			errors['password'] = "Incorrect password!"
		return errors

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=100)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	objects = UserManager()