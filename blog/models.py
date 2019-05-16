from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    auther=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    sub_title=models.CharField(max_length=200)
    text=models.TextField(null=False,blank=False)
    created_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField()

def publish(self):
    self.published_date=timezone.now()
    self.save()

def _str_(self):
    return self.title
