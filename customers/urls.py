from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    # Customers Lists - active and inactive
    path('all/', views.CustomerList.as_view(), name='customer_list'),
    path('all/deactivated/', views.DeactivatedCustomerList.as_view(), name='deactivated_customer_list'),

    # Customer Profile Information - Basic Info, Orders and Coupons
    path('<int:pk>/', views.CustomerProducts.as_view(), name='customer_orders'),

    # Customer Create-Update
    path('new/', views.CustomerCreate.as_view(), name='customer_create'),
    path('<int:pk>/update/', views.CustomerUpdate.as_view(), name='customer_update'),

    # Customer Deletion/(De)activation
    path('<int:pk>/delete/', views.CustomerDelete.as_view(), name='customer_delete'),
    path('<int:pk>/deactivate/', views.CustomerDeactivate.as_view(), name='customer_deactivate'),
    path('<int:pk>/activate/', views.CustomerReactivate.as_view(), name='customer_reactivate'),

    # Search
    path('search/', views.CustomerSearch.as_view(), name='customer_search'),

    # Coupons
    path('<int:customer_pk>/new_coupon/', views.CouponAdd.as_view(), name='customer_coupon_add'),
    path('<int:pk>/coupon_delete/', views.CouponDelete.as_view(), name='coupon_delete'),

]
