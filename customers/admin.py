from django.contrib import admin
from .models import Customer, Coupon

# Register your models here.

admin.site.register(Customer)
admin.site.register(Coupon)