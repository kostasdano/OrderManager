from django.db import models
from django.urls import reverse


class Customer(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    full_name = models.CharField(max_length=121)
    email = models.EmailField()
    birth_date = models.DateField()
    tin = models.PositiveIntegerField()
    c_active = models.BooleanField(default=True)    # if c_active=False, Customer is unavailable for Orders/Search while existing Orders don't get deleted


    def save(self, *args, **kwargs):
        self.full_name = self.first_name + ' ' + self.last_name
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('customers:customer_orders', kwargs={'pk': self.pk})

    @property
    def display_name(self):
        return f'{self.first_name} {self.last_name}'


class Coupon(models.Model):
    code = models.CharField(max_length=10, unique=True)
    discount_percentage = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, related_name="coupons", on_delete=models.CASCADE)       # Multiple coupons to each Customer

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse('customers:customer_orders', kwargs={'pk': self.customer.pk})


