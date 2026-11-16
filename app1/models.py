from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    stock_min = models.IntegerField()
    precio = models.FloatField()


    def __str__(self):
        return self.nombre+"-Stock disponible: "+str(self.stock)
