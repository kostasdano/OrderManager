from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    p_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_details', kwargs={'pk': self.pk})
