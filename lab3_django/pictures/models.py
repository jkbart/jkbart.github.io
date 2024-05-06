from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

# Create your models here.
class Drawing(models.Model):
    author = models.ManyToManyField(User)
    width = models.IntegerField(default=100)
    height = models.IntegerField(default=100)
    name = models.CharField(max_length=200, default="Not named")
    pub_date = models.DateTimeField("date published")
    description = models.CharField(max_length=1000, blank=True, default='')
    tags = models.ManyToManyField(Tag)

class Rectangle(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    color = models.CharField(max_length=50, default="black")
    author = models.ForeignKey(Drawing, on_delete=models.CASCADE) 