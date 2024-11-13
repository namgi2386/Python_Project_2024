from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=255)
    image = models.ImageField(blank=True , upload_to='images/')
    point = models.IntegerField(blank=True,null=True ,default=5 )