from django.db import models

# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    