from django.db import models
from django.urls import reverse
from products.models import Product
from customers.models import Customer



class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer_orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_orders', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('customer', 'product')

    def get_absolute_url(self):
        return reverse('orders:order_details', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {} -> {} ({})'.format(self.customer.first_name, self.customer.last_name, self.product.name, self.amount)


