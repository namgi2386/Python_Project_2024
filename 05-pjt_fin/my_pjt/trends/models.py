from django.db import models

# Create your models here.

class Keyword(models.Model):
    name =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Trend(models.Model):
    name =models.TextField()
    result = models.IntegerField(blank=True, null=True, default=777)
    search_period = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
