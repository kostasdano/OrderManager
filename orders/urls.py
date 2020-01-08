from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
    path('', views.OrderList.as_view(), name='order_list'),
    path('new/', views.OrderCreate.as_view(), name='order_create'),
    path('new/for_customer/<int:customer_pk>', views.OrderCreate.as_view(), name='order_create_cpk'),
    path('new/for_product/<int:product_pk>', views.OrderCreate.as_view(), name='order_create_ppk'),
    path('<int:pk>/', views.OrderDetails.as_view(), name='order_details'),
    path('<int:pk>/delete/', views.OrderDelete.as_view(), name='order_delete'),
    path('<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),
]