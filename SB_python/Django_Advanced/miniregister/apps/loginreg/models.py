from __future__ import unicode_literals

from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def validateName(name):
	if len(name) < 3:
		raise ValidationError(
			'{} must be at least 3 characters.'.format(value)
		)

def validateEmail(email):
	if not validate_email(email)
		raise ValidationError(
			'{} incorrect format.'.format(value)
		)


def validatePass(password):
	if len(password) < 8:
		raise ValidationError(
			'{} must be at least 8 characters.'.format(value)
		)

class User(models.Model):
	first_name = models.CharField(max_length=255, validators = [validateName])
	last_name = models.CharField(max_length=255, validators = [validateName])
	email = models.EmailField(validators = [validateEmail])
	password = models.CharField(max_length=100, validators = [validatePass])