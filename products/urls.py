from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # Products Lists - active and inactive
    path('all/', views.ProductList.as_view(), name='product_list'),
    path('all/deactivated', views.DeactivatedProductList.as_view(), name='deactivated_product_list'),

    # Product Profile Information - Basic Info, Orders and Coupons
    path('<int:pk>/', views.ProductsCostumers.as_view(), name='product_details'),

    # Product Create-Update
    path('new/', views.ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/update', views.ProductUpdate.as_view(), name='product_update'),

    # Product Deletion/(De)activation
    path('<int:pk>/delete', views.ProductDelete.as_view(), name='product_delete'),
    path('<int:pk>/deactivate/', views.ProductDeactivate.as_view(), name='product_deactivate'),
    path('<int:pk>/activate/', views.ProductReactivate.as_view(), name='product_reactivate'),

    # Search
    path('search/', views.ProductSearch.as_view(), name='product_search'),
]
