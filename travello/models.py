from django.db import models


# Create your models here.


class Destination(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    address = models.CharField(max_length=200, null=True)
    offer = models.BooleanField(default=False)
    location_type = models.CharField(max_length=100, null=True)
    location_url = models.URLField(null=True)


class parks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    address = models.CharField(max_length=200, null=True)
    location_type = models.CharField(max_length=100, null=True)
    location_url = models.URLField(null=True)


class parksnearby(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    address = models.CharField(max_length=200, null=True)
    location_type = models.CharField(max_length=100, null=True)
    location_url = models.URLField(null=True)
