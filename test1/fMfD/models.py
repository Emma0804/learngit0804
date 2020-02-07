#test1/4M4D/models.py
from django.db import models
class Comment(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pub_house = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
class Comments(models.Model):
    content = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')