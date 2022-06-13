from django.db import models

# Create your models here.
class User(models.Model):
    nama = models.CharField(max_length=255)
    npm = models.CharField(max_length=10, unique=True)