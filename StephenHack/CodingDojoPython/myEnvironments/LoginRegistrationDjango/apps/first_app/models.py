from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[^\W_]+(-[^\W_]+)?$')

class UserManager(models.Manager):
	def register(self, first_name, last_name, email, password, conf_password):
		errors = [] #will hold errors
		if len(email) == 0:
			errors.append("No email entered.")
		elif not EMAIL_REGEX.match(email):
			errors.append("Email not formatted correctly.")
		if len(first_name) < 2:
			errors.append("First Name has to be at least 2 characters!")
		elif not NAME_REGEX.match(first_name):
			errors.append("First name not formatted correctly")
		if len(last_name) < 2:
			errors.append("Last Name has to be at least 2 characters!")
		elif not NAME_REGEX.match(last_name):
			errors.append("Last name not formatted correctly")
		if len(password) < 8:
			errors.append("Password needs to be least 8 characters!")
		elif (password != conf_password):
			errors.append("Passwords must match!!")
		if len(errors) is not 0:
			return (False, errors)
		else:
			# pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

			# check if this is working
			u = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
			# u.save()
			return (True, u)

	def login(self, email, password):
		login_errors = [] #will hold errors
		if len(email) == 0:
			login_errors.append("No email entered.")
		elif not EMAIL_REGEX.match(email):
			login_errors.append("Email not formatted correctly.")
		if len(password) < 8:
			login_errors.append("Password needs to be least 8 characters!")
		# print login_errors
		if len(login_errors) is 0:
			# try:
				print email
				print password
				user = User.objects.get(email=email, password=password)
				print user
				# password = request.POST['password'].encode()
				# if bcrypt.hashpw(password, user.pw_hash.encode()):
				if user:
					return (True, user)
				else:
					return (False, ["Email/Password does not match"])
			# except ObjectDoesNotExist:
				# pass


class User(models.Model):
	first_name = models.CharField(max_length=70)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	password = models.CharField(max_length=100)

	objects = UserManager()
	# userMgr = UserManager()
