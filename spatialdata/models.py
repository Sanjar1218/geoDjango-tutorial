from django.contrib.gis.db import models

class Zipcode(models.Model):
    address = models.CharField(max_length=255)
    home = models.PolygonField()
