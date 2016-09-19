from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Email(models.Model):
	email = models.EmailField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)