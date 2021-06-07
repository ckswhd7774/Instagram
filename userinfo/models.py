from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import OneToOneField
from behaviors import BaseFiled
# Create your models here.
class Profile(BaseFiled) :
    user = OneToOneField(User, on_delete=models.SET_NULL, related_name='profile', null=True, blank=True)
    name = models.CharField(max_length=32)
    introduce = models.TextField()
    address = models.TextField()    
