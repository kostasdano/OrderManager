from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from products.models import Product
from customers.models import Customer


class HomePage(TemplateView):
    template_name = 'index.html'


class HomeSearch(LoginRequiredMixin, ListView):
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('keyword')

        if len(query) != 0:
            # Products Results
            self.product_results = Product.objects.filter(
                Q(name__icontains=query) & Q(p_active=True)
            )

            # Customer Results
            # search for first or last name
            self.customer_results = Customer.objects.filter(
                (Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(full_name__icontains=query))
                & Q(c_active=True)
            )

            # Order Results - this one's tricky
            customer_order_results = []
            product_order_results = []
            if self.product_results is not None:
                for product in self.product_results:
                    product_order_results.append(product.product_orders.all())

            if self.customer_results is not None:
                for customer in self.customer_results:
                    customer_order_results.append(customer.customer_orders.all())

            self.customer_order_results = customer_order_results
            self.product_order_results = product_order_results
            # Return
            return self.product_results, self.customer_results, self.customer_order_results, self.product_order_results
        else:
            self.product_results = None
            self.customer_results = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.customer_results:
            if not self.product_results:
                context["keyword"] = self.request.GET.get('keyword')
                context["results"] = False
                return context
        context["results"] = True
        context["product_results"] = self.product_results
        context["customer_results"] = self.customer_results
        context["customer_order_results"] = self.customer_order_results
        context["product_order_results"] = self.product_order_results
        context["keyword"] = self.request.GET.get('keyword')
        return context
