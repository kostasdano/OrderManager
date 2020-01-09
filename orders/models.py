from django.db import models
from django.urls import reverse
from products.models import Product
from customers.models import Customer, Coupon



class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer_orders', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_orders', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    coupon = models.OneToOneField(Coupon, related_name="order", blank=True, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('customer', 'product')

    def get_absolute_url(self):
        return reverse('orders:order_details', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} ordered {}'.format(self.customer.full_name, self.product.name)


