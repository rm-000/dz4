from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40, blank=False)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f'{self.name} - {self.price}'

class ProductComment(models.Model):
    user_name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=60, blank=False)
    feedback = models.CharField(null=True, max_length=300, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return f'Отзыв от {self.user_name}: {self.product}'
