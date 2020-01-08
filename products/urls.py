from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('new', views.ProductCreate.as_view(), name='product_create'),
    path('<int:pk>/', views.ProductsCostumers.as_view(), name='product_details'),
    path('<int:pk>/update', views.ProductUpdate.as_view(), name='product_update'),
    path('<int:pk>/delete', views.ProductDelete.as_view(), name='product_delete'),
    path('<int:pk>/deactivate/', views.ProductDeactivate.as_view(), name='product_deactivate'),
    path('<int:pk>/activate/', views.ProductReactivate.as_view(), name='product_reactivate'),
    path('search/', views.ProductSearch.as_view(), name='product_search'),
]
