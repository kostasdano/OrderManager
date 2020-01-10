from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Order List
    path('all/', views.OrderList.as_view(), name='order_list'),

    # Order Details
    path('<int:pk>/', views.OrderDetails.as_view(), name='order_details'),

    # Create Order
    path('new/', views.OrderCreate.as_view(), name='order_create'),
    path('ajax/load-coupons/', views.load_coupons, name='ajax_load_coupons'),

    # Order Update
    path('<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),

    # Order Delete / Single or Multiple
    path('<int:pk>/delete/', views.OrderDelete.as_view(), name='order_delete'),
    path('all/delete/', views.DeleteMultipleOrders.as_view(), name='delete_orders'),
]
