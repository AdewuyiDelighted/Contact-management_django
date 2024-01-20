from django.db import models


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    password = models.CharField(max_length=25)
    is_Locked = models.BooleanField(default=False)


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=25)
    address = models.CharField(max_length=150)
    userEmail = models.CharField(max_length=50)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
