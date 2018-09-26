from django.db import models

# Create your models here.
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    website=models.URLField()
