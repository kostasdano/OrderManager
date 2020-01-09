from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import  get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms.widgets import SelectDateWidget
from .models import Customer, Coupon


class CustomerList(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/list.html'

    def get_queryset(self):
        return Customer.objects.filter(c_active=True)

    paginate_by = 4


class DeactivatedCustomerList(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/list.html'

    def get_queryset(self):
        return Customer.objects.filter(c_active=False)

    paginate_by = 4



class CustomerSearch(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/list.html'

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        object_list = Customer.objects.filter(
            (Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(full_name__icontains=query))
            & Q(c_active=True)
        )
        return object_list



class CustomerCreate(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'email', 'birth_date', 'tin']
    template_name = 'customers/create_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.form_class
        form = super(CustomerCreate, self).get_form(form_class)
        form.fields['birth_date'].widget = SelectDateWidget(years=range(1900, 2002))
        return form


class CustomerProducts(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/details.html'
    paginate_by = 4

    def get_queryset(self):
        self.customer = get_object_or_404(Customer, pk=self.kwargs['pk'])
        return self.customer.customer_orders.all(), self.customer.coupons.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customer"] = self.customer
        context["order_list"] = self.customer.customer_orders.all()
        context["coupon_list"] = self.customer.coupons.all()
        return context


class CustomerUpdate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['tin', 'email']
    template_name = 'customers/update_form.html'

    def get_success_url(self):
        return reverse_lazy('customers:customer_orders', kwargs={'pk': self.object.pk})


class CustomerDeactivate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['c_active']
    template_name = 'customers/deletion_options.html'

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        request.POST['c_active'] = False
        return super(CustomerDeactivate, self).post(request, **kwargs)

    def get_success_url(self):
        return reverse_lazy('customers:customer_orders', kwargs={'pk': self.object.pk})


class CustomerReactivate(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['c_active']
    template_name = 'customers/confirm_activation.html'

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        request.POST['c_active'] = True
        return super(CustomerReactivate, self).post(request, **kwargs)

    def get_success_url(self):
        return reverse_lazy('customers:customer_orders', kwargs={'pk': self.object.pk})


class CustomerDelete(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers/deletion_options.html'

    def get_success_url(self):
        return reverse_lazy('customers:customer_list')


# Coupon Classes


class CouponAdd(LoginRequiredMixin, CreateView):
    model = Coupon
    fields = ['code', 'discount_percentage', 'customer']
    template_name = 'customers/add_coupon.html'

    def get_form(self, *args, **kwargs):
        form = super(CouponAdd, self).get_form(*args, **kwargs)
        form.fields['customer'].queryset = Customer.objects.filter(c_active=True)
        return form

    def get_initial(self):
        initial = super(CouponAdd, self).get_initial()
        if "customer_pk" in self.kwargs:
            customer = Customer.objects.get(id=self.kwargs.get("customer_pk"))
            initial['customer'] = customer
        return initial


class CouponDelete(LoginRequiredMixin, DeleteView):
    model = Coupon

    def delete(self, *args, **kwargs):
        self.customer = Coupon.objects.get(id=self.kwargs.get("pk")).customer.pk
        self.object = self.get_object()
        return super().delete(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('customers:customer_orders', kwargs={'pk': self.customer})

