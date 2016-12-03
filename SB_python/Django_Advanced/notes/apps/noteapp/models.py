from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Note(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=255)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)