from django.db import models
from django.contrib.postgres.fields import ArrayField
class Library(models.Model):
    bookId= models.IntegerField(primary_key=True)
    bookName= models.CharField(max_length=100)
    publishDate= models.DateTimeField()
    available= models.IntegerField(null=True)
    author= models.CharField(null=True, max_length=100)

class Users(models.Model):
    uname= models.CharField(primary_key=True, max_length=30)
    pwd= models.CharField(max_length=30)
    rented= ArrayField(models.IntegerField(), null=True)
    due= models.DateTimeField(null=True)

class Admins(models.Model):
    uname = models.CharField(primary_key=True, max_length=30)
    pwd = models.CharField(max_length=30)
