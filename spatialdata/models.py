from django.contrib.gis.db import models

class Zipcode(models.Model):
    address = models.CharField(max_length=255)
    home = models.PolygonField()
    way = models.MultiLineStringField()

    def __str__(self):
        return str(self.address)
