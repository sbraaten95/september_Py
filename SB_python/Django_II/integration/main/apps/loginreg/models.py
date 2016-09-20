from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt

# Create your models here.

class UserManager(models.Manager):
	def login(self, email, password):
		errors = {}
		if len(password) < 8:
			errors['password'] = 'Incorrect password'
			return errors

		user = User.objects.get(email = email)
		password = password.encode()
		if not bcrypt.hashpw(password, user.password.encode()):
			errors['password'] = 'Incorrect password'
		return errors

	def register(self, first_name, last_name, email, password, dblcheck):
		errors = {}

		if len(first_name) < 2:
			print len(first_name)
			errors['first_name'] = 'First name too short!'
		for c in first_name:
			if not c.isalpha():
				errors['first_name'] += 'First name must only be letters!'
		print errors

		if len(last_name) < 2:
			errors['last_name'] = 'Last name too short!'
		for c in last_name:
			if not c.isalpha():
				errors['last_name'] += 'Last name must only be letters!'

		try:
			validate_email(email)
		except ValidationError:
			errors['email'] = 'Email incorrect format!'

		if len(password) < 8:
			errors['password'] = 'Password too short!'

		return errors


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	objects = UserManager()