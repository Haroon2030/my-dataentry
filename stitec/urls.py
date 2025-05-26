from django.urls import path
from . import views

app_name = 'stitec'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('products/', views.product_list, name='products'),
    path('supplier-matching/', views.supplier_matching_list, name='supplier_matching'),
    path('supplier-matching/export/<str:format>/', views.export_supplier_matching, name='export_matching'),
]
