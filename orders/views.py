from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from customers.models import Customer
from products.models import Product
from .models import Order


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/list.html'
    queryset = Order.objects.all().order_by('-date')
    paginate_by = 6


class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['customer', 'product', 'amount']
    template_name = 'orders/create_form.html'

    def get_form(self, *args, **kwargs):
        form = super(OrderCreate, self).get_form(*args, **kwargs)
        form.fields['customer'].queryset = Customer.objects.filter(c_active=True)
        form.fields['product'].queryset = Product.objects.filter(p_active=True)
        return form

    def get_initial(self):
        initial = super(OrderCreate, self).get_initial()
        if "customer_pk" in self.kwargs:
            customer = Customer.objects.get(id__iexact=self.kwargs.get("customer_pk"))
            initial['customer'] = customer
        elif "product_pk" in self.kwargs:
            product = Product.objects.get(id__iexact=self.kwargs.get("product_pk"))
            initial['product'] = product
        return initial



class OrderDetails(LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/details.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # add total price
        ctx['total_price'] = ctx['order'].amount * ctx['order'].product.price

        return ctx


class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'orders/confirm_delete.html'

    def delete(self, *args, **kwargs):
        self.customer = Order.objects.get(id__iexact=self.kwargs.get("pk")).customer.pk
        self.object = self.get_object()
        return super().delete(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('customers:customer_orders', kwargs={'pk': self.customer})


class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['amount']
    template_name = 'orders/update_form.html'

    def get_success_url(self):
        return reverse_lazy('orders:order_details', kwargs={'pk': self.object.pk})