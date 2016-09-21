from __future__ import unicode_literals
from django.db import models
from ..login_registration.models import User

class userManager(models.Manager):
    def validatePresence(self, postData):

        if len(postData['name']) > 0 and len(postData['description']) > 0:
            return True
        else:
            return False

class Courses(models.Model):
	user = models.ManyToManyField('login_registration.User')
	name = models.CharField(max_length=255)
	description = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = userManager()
