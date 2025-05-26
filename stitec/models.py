from django.db import models
from django.utils import timezone

# Create your models here.
class Unit(models.Model):
    """نموذج الوحدة"""
    name = models.CharField(max_length=100, verbose_name="اسم الوحدة")
    code = models.CharField(max_length=20, verbose_name="رمز الوحدة", unique=True)
    description = models.TextField(verbose_name="الوصف", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "الوحدة"
        verbose_name_plural = "الوحدات"
        ordering = ['name']


class Supplier(models.Model):
    """نموذج المورد"""
    name = models.CharField(max_length=255, verbose_name="اسم المورد")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "المورد"
        verbose_name_plural = "الموردين"
        ordering = ['-created_at']


class Product(models.Model):
    """نموذج المنتج"""
    name = models.CharField(max_length=255, verbose_name="اسم الصنف")
    barcode = models.CharField(max_length=20, verbose_name="الباركود", unique=True)
    unit = models.ForeignKey(Unit, on_delete=models.PROTECT, related_name='products', verbose_name="الوحدة")
    package_size = models.CharField(max_length=50, verbose_name="حجم العبوة", blank=True, null=True, help_text="مثال: 20-24-36")
    sender_name = models.CharField(max_length=255, verbose_name="اسم المرسل")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products', verbose_name="المورد")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "المنتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']


class SupplierMatching(models.Model):
    """نموذج مطابقة المورد"""
    STATUS_CHOICES = [
        ('complete', 'مكتمل'),
        ('partial', 'جزئي'),
        ('pending', 'معلق'),
    ]

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='matchings', verbose_name="المورد")
    matching_file_name = models.CharField(max_length=50, verbose_name="اسم ملف المطابقة")
    matching_file = models.FileField(upload_to='matching_files/', verbose_name="ملف المطابقة", help_text="يمكن تحميل ملفات PDF أو Word")
    accountant_name = models.CharField(max_length=255, verbose_name="اسم المحاسب")
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المديونية")
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="السداد")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="الحالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    
    def __str__(self):
        return f"{self.supplier.name} - {self.matching_file_name}"

    class Meta:
        verbose_name = "مطابقة المورد"
        verbose_name_plural = "مطابقات الموردين"
        ordering = ['-created_at']
