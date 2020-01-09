from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product


class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/list.html'

    def get_queryset(self):
        return Product.objects.filter(p_active=True)

    paginate_by = 4


class DeactivatedProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/list.html'

    def get_queryset(self):
        return Product.objects.filter(p_active=False)

    paginate_by = 4


class ProductSearch(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/list.html'

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        object_list = Product.objects.filter(
            Q(name__icontains=query) & Q(p_active=True)
        )
        return object_list


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'price']
    template_name = 'products/create_form.html'


class ProductsCostumers(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/details.html'
    paginate_by = 4

    def get_queryset(self):
        self.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return self.product.product_orders.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = self.product
        return context


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/update_form.html'
    fields = ['description', 'price']

    def get_success_url(self):
        return reverse_lazy('products:product_details', kwargs={'pk': self.object.pk})


class ProductDeactivate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['p_active']
    template_name = 'products/deletion_options.html'

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        request.POST['p_active'] = False
        return super(ProductDeactivate, self).post(request, **kwargs)

    def get_success_url(self):
        return reverse_lazy('products:product_details', kwargs={'pk': self.object.pk})


class ProductReactivate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['p_active']
    template_name = 'products/confirm_activation.html'

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        request.POST['p_active'] = True
        return super(ProductReactivate, self).post(request, **kwargs)

    def get_success_url(self):
        return reverse_lazy('products:product_details', kwargs={'pk': self.object.pk})


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/deletion_options.html'
    success_url = reverse_lazy('products:product_list')
