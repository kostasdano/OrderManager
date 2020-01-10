from decimal import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, FormView
from customers.models import Customer
from .models import Order
from .forms import OrderForm, CheckboxesForm


# List of all Orders
class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/list.html'
    queryset = Order.objects.all().order_by('-date')
    paginate_by = 6


# Create Order
class OrderCreate(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'orders/create_form.html'
    form_class = OrderForm


# Load Coupon dropdown list for OrderCreate form
def load_coupons(request):
    customer_id = request.GET.get('customer')
    customer = Customer.objects.get(id=customer_id)
    coupons = customer.coupons.filter(order=None)
    return render(request, 'orders/coupon_dropdown_list_options.html', {'coupons': coupons})


# Order Details
class OrderDetails(LoginRequiredMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/details.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # Calculate discount, if coupon exists
        if ctx['order'].coupon:
            ctx['initial_price'] = ctx['order'].amount * ctx['order'].product.price
            ctx['total_price'] = round(Decimal(ctx['initial_price'] - Decimal(ctx['initial_price']) * Decimal(ctx['order'].coupon.discount_percentage/100)), 2)
        else:
            ctx['total_price'] = ctx['order'].amount * ctx['order'].product.price
        return ctx


# Delete Order
class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order

    def delete(self, *args, **kwargs):
        self.customer = Order.objects.get(id=self.kwargs.get("pk")).customer.pk
        self.object = self.get_object()
        return super().delete(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('customers:customer_orders', kwargs={'pk': self.customer})


# Edit Order
class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['amount']
    template_name = 'orders/update_form.html'

    def get_success_url(self):
        return reverse_lazy('orders:order_details', kwargs={'pk': self.object.pk})


# Delete Multiple Orders / Uses Checkboxes Form
class DeleteMultipleOrders(LoginRequiredMixin, FormView):
    form_class = CheckboxesForm
    template_name = 'orders/delete_multiple_orders.html'

    def get_context_data(self, **kwargs):
        context = super(DeleteMultipleOrders,self).get_context_data(**kwargs)
        context['order_list'] = Order.objects.all()
        return context

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['checkboxes'].queryset = Order.objects.all()
        return form

    def form_valid(self, form):
        qs = Order.objects.filter(
            pk__in=list(map(int, self.request.POST.getlist('checkboxes')))
        )
        qs.delete()
        return HttpResponseRedirect(reverse_lazy('orders:order_list'))

