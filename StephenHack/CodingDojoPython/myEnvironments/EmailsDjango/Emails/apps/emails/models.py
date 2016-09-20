from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class EmailManager(models.Manager): #A Manager is the interface through which database query operations are provided to Django models. At least one Manager exists for every model in a Django application.
    def register(self, email):
        errors = [] #creates an empty array to hold errors
        if len(email) == 0:
            errors.append("Email is required") #appends to array error
        elif not EMAIL_REGEX.match(email): 
            errors.append("Invalid Email")
        if len(errors) is not 0: 
            return (False, errors) #returning boolean, and array
        else:
            e = Email.emailMgr.create(email=email) # creates an object e with email
            e.save() 
            return (True, e) 

    def destroy(self, id):
        e = Email.emailMgr.get(id=id)
        if not e:
            return (False, "No Email Found With That ID")
        else:
            e.delete()
            return (True, "Email Deleted")

class Email(models.Model):
    email = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    emailMgr = EmailManager() #our model manager
