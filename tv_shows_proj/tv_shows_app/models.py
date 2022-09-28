import datetime
import time
from distutils.log import error
from email.policy import default
from time import strftime
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors={}
        if len(postData['title']) < 2:
            errors['title']="Title length should be > 2"
        if len(postData['network']) < 3:
            errors['network']="Network length should be > 3"
        if len(postData['desc']) < 10:
            errors['desc']="Description should be > 10"
        if postData['release_date']>datetime.date.today().isoformat():
            errors['release_date']="Date should be before today"

        return errors

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=50)
    release_date=models.DateField()
    desc=models.TextField(default="")
    objects=ShowManager()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


