from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailManager(models.Manager):
	def register(self, email):
		errors = []
		if len(email) == 0:
			errors.append('Email is Required')
		elif not EMAIL_REGEX.match(email):
			errors.append('Email is in the wrong format')
		if len(errors) is not 0:
			return (False, errors)
		else:
			e = Email.emailMgr.create(email=email)
			e.save()
			return (True, e)

	def destroy(self, id):
		e = Email.emailMgr.get(id=id)
		if not e:
			return (False, "No Email Found With That ID")
		else:
			e.delete()
			return (True, "Email Deleted")

# Create your models here.
class Email(models.Model):
	email = models.EmailField(max_length=70)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	emailMgr = EmailManager()

