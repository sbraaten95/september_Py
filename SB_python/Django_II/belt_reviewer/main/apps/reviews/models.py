from __future__ import unicode_literals

from django.db import models

from ..loginregister.models import User

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class Review(models.Model):
	user = models.ForeignKey(User)
	book = models.ForeignKey(Book)
	review = models.TextField()
	rating = models.IntegerField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)