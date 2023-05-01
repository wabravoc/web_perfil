from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class user_contact(models.Model):
    first_name=models.CharField(max_length=50, blank=True)
    last_name=models.CharField(max_length=50, blank=True)
    celphone=models.IntegerField()
    email=models.EmailField()
    message=models.CharField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    def serialize(self):
        return{
            "id":self.id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "celphone":self.celphone,
            "email":self.email,
            "mensaje":self.mensaje,  
            "timestamp":self.timestamp.strftime("%b %d %Y, %I:%M %p"),   
        }
    