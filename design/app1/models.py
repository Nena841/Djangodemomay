from django.db import models


# Create your models here.
class Place(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)


class Team(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
