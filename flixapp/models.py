from django.db import models
from adminapp.models import*

class Register(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} -- {self.email}"
    
class Singlearea(models.Model):
    movie=models.CharField(max_length=20)
    tvseries=models.CharField(max_length=20)
    music=models.CharField(max_length=20)

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=150)
    areas=models.CharField(max_length=20)
    comment=models.CharField(max_length=200)
    rating=models.IntegerField(default=0)





# Create your models here.
