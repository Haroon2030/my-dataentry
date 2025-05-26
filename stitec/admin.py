from django.contrib import admin
from .models import Supplier, Product, SupplierMatching, Unit

# Register your models here.
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'description', 'created_at']
    search_fields = ['name', 'code']
    list_filter = ['created_at']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'barcode', 'unit', 'package_size', 'supplier', 'sender_name', 'created_at']
    search_fields = ['name', 'barcode', 'sender_name', 'package_size']
    list_filter = ['unit', 'supplier', 'created_at']
    autocomplete_fields = ['supplier', 'unit']


@admin.register(SupplierMatching)
class SupplierMatchingAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'matching_file_name', 'matching_file', 'accountant_name', 'debt_amount', 'payment_amount', 'status', 'created_at']
    search_fields = ['supplier__name', 'matching_file_name', 'accountant_name']
    list_filter = ['status', 'created_at']
    autocomplete_fields = ['supplier']
    list_editable = ['status']
