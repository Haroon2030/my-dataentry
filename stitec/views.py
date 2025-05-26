from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Sum
from django.contrib import messages
from django.db.models import F, Q
from .models import Supplier, Product, SupplierMatching, Unit

# Create your views here.
def dashboard(request):
    """عرض لوحة التحكم الرئيسية"""
    
    # إحصائيات للوحة التحكم
    total_products = Product.objects.count()
    total_suppliers = Supplier.objects.count()
    total_debt = SupplierMatching.objects.aggregate(total=Sum('debt_amount'))['total'] or 0
    completed_matches = SupplierMatching.objects.filter(status='complete').count()
    total_matches = SupplierMatching.objects.count()
    
    completion_rate = 0
    if total_matches > 0:
        completion_rate = (completed_matches / total_matches) * 100
    
    # أحدث المنتجات
    recent_products = Product.objects.select_related('supplier').order_by('-created_at')[:4]
    
    # أحدث مطابقات الموردين
    recent_matchings = SupplierMatching.objects.select_related('supplier').order_by('-created_at')[:4]
    
    context = {
        'total_products': total_products,
        'total_suppliers': total_suppliers,
        'total_debt': total_debt,
        'completion_rate': completion_rate,
        'recent_products': recent_products,
        'recent_matchings': recent_matchings,
    }
    
    return render(request, 'dashboard.html', context)


def product_list(request):
    """عرض قائمة المنتجات"""
    search_query = request.GET.get('search', '')
    
    if search_query:
        products = Product.objects.filter(
            Q(name__icontains=search_query) |
            Q(barcode__icontains=search_query) |
            Q(supplier__name__icontains=search_query) |
            Q(sender_name__icontains=search_query)
        ).select_related('supplier', 'unit')
    else:
        products = Product.objects.select_related('supplier', 'unit').all()
    
    context = {
        'products': products,
        'search_query': search_query,
    }
    
    return render(request, 'products.html', context)


def supplier_matching_list(request):
    """عرض قائمة مطابقات الموردين"""
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    
    # البحث والتصفية
    matchings_query = SupplierMatching.objects.select_related('supplier')
    
    if search_query:
        matchings_query = matchings_query.filter(
            Q(supplier__name__icontains=search_query) |
            Q(matching_file_name__icontains=search_query) |
            Q(accountant_name__icontains=search_query)
        )
    
    if status_filter:
        matchings_query = matchings_query.filter(status=status_filter)
    
    # الإحصائيات
    total_matchings = SupplierMatching.objects.count()
    completed_matchings = SupplierMatching.objects.filter(status='complete').count()
    pending_matchings = SupplierMatching.objects.filter(status__in=['pending', 'partial']).count()
    
    context = {
        'matchings': matchings_query,
        'search_query': search_query,
        'status_filter': status_filter,
        'total_matchings': total_matchings,
        'completed_matchings': completed_matchings,
        'pending_matchings': pending_matchings,
    }
    
    return render(request, 'supplier_matching_enhanced.html', context)


"""
تم إزالة جميع وظائف الإجراءات ذات الصلة بمطابقات الموردين حسب الطلب
"""

def export_supplier_matching(request, format):
    """تصدير مطابقات الموردين بتنسيق معين"""
    # سيتم تنفيذ هذه الوظيفة لاحقًا
    messages.success(request, f'جاري تطوير خاصية التصدير بتنسيق {format}')
    return redirect('stitec:supplier_matching')
