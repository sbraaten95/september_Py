from __future__ import unicode_literals
from django.db import models
from ..login_registration.models import User

class Book(models.Model):
	name = models.CharField(max_length= 255)
	author = models.CharField(max_length=45, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
class Review(models.Model):
	book = models.ForeignKey(Book)
	user = models.ForeignKey(User)
	rating = models.IntegerField()
	review = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)