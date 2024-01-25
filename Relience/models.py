from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 50)
    Brand = models.CharField(max_length = 50)
    waranty = models.CharField(max_length = 50)
    price = models.FloatField()
    is_available = models.BooleanField(default = False)


    def __str__(self):
        return f"{self.name}"


    class Meta():
        db_table = "Product"



