from django.db import models

# Create your models here.

class Personal(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    address = models.TextField()
    phone_num = models.CharField(max_length=10)
    image = models.ImageField()
