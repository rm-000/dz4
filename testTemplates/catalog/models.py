from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40, blank=False)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f'{self.name} - {self.price}'