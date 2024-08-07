from django.db import models
from mongoengine import EmailField,StringField,BooleanField,Document
from django.contrib.auth.hashers import make_password,check_password


# Create your models here.

class MongoTable(Document):
    name=StringField(max_length=50)
    email=EmailField()
    password=StringField(max_length=128)
    
    # def save(self,*args,**kwargs):
    #     user=MongoTable.objects.filter(email=self.email).first()
    #     if not user:
    #         self.password=make_password(self.password)
    #     super().save(*args,**kwargs)
class MongoToken(Document):
    userId=StringField(max_length=128)
    email=EmailField()
    token=StringField(max_length=255)