from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('all/', views.CustomerList.as_view(), name='customer_list'),
    path('<int:pk>/orders/', views.CustomerProducts.as_view(), name='customer_orders'),
    path('new/', views.CustomerCreate.as_view(), name='customer_create'),
    path('<int:customer_pk>/new_coupon/', views.CouponAdd.as_view(), name='customer_coupon_add'),
    path('<int:pk>/coupon_delete/', views.CouponDelete.as_view(), name='coupon_delete'),
    path('<int:pk>/delete/', views.CustomerDelete.as_view(), name='customer_delete'),
    path('<int:pk>/deactivate/', views.CustomerDeactivate.as_view(), name='customer_deactivate'),
    path('<int:pk>/activate/', views.CustomerReactivate.as_view(), name='customer_reactivate'),
    path('<int:pk>/update/', views.CustomerUpdate.as_view(), name='customer_update'),
    path('search/', views.CustomerSearch.as_view(), name='customer_search'),
]
