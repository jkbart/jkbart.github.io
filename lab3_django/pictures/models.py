from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Drawing(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="Not named")
    pub_date = models.DateTimeField("date published")

class Rectangle(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    color = models.CharField(max_length=50, default="black")
    author = models.ForeignKey(Drawing, on_delete=models.CASCADE) 