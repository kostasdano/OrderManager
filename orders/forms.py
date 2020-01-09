from django import forms
from customers.models import Customer, Coupon
from products.models import Product
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('customer', 'product', 'amount', 'coupon')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coupon'].queryset = Coupon.objects.none()
        self.fields['product'].queryset = Product.objects.filter(p_active=True)
        self.fields['customer'].queryset = Customer.objects.filter(c_active=True)

        if 'customer' in self.data:
            try:
                customer_id = self.data.get('customer')
                customer = Customer.objects.get(id=customer_id)
                self.fields['coupon'].queryset = customer.coupons.filter(order=None)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['coupon'].queryset = self.instance.customer.coupons.all()



class CheckboxesForm(forms.Form):

    checkboxes = forms.ModelMultipleChoiceField(
        Order.objects.all(),
        label='',
        widget=forms.CheckboxSelectMultiple)

