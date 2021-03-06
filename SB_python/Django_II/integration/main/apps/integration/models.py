from __future__ import unicode_literals

from django.db import models

from ..courses.models import Course
from ..loginreg.models import User

# Create your models here.
class Merge(models.Model):
	course = models.ForeignKey(Course)
	user = models.ForeignKey(User)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)