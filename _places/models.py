from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)

class Place(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    # geo = models.geo



