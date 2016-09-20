from __future__ import unicode_literals

from django.db import models
from ..loginreg.models import User

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	course_taker = models.ForeignKey(User)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)