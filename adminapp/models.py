from django.db import models
from flixapp.models import*


# Create your models here.

class Categories(models.Model):
    image=models.ImageField(upload_to='image',default='null.jpg')
    title=models.CharField(max_length=25)
    description=models.CharField(max_length=30)
    releaseyear=models.IntegerField(default=0)
    runtime=models.IntegerField(default=0)
    quality=models.CharField(max_length=10)
    country=models.CharField(max_length=20)
    genre=models.CharField(max_length=20)
    area=models.CharField(max_length=10)
    video=models.FileField(upload_to='video',default='null.mkv')
    audio=models.FileField(upload_to='audio',default='null.mp3')
    link=models.CharField(max_length=20)
    


class SubscriptionPlan(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField(default=0)
    validity=models.IntegerField()
    features=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)


class Subscribed_users(models.Model):
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE)
    plan_id=models.ForeignKey(SubscriptionPlan,on_delete=models.DO_NOTHING)
    subscribed_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=100,default="INACTIVE")
    expiry_date=models.DateTimeField(null=True, blank=False)





    

