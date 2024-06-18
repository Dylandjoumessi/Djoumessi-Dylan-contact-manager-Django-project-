from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.name
