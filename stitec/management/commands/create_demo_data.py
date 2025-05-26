from django.core.management.base import BaseCommand
from django.utils import timezone
from stitec.models import Supplier, Product, SupplierMatching, Unit
import random

class Command(BaseCommand):
    help = 'إنشاء بيانات تجريبية للنظام'

    def handle(self, *args, **kwargs):
        self.stdout.write('جاري إنشاء بيانات تجريبية...')
        
        # إنشاء الموردين
        supplier_names = [
            'شركة الوطن للتجارة',
            'مؤسسة النور التجارية',
            'شركة الفا للاستيراد',
            'مؤسسة العالمية للتوريدات',
            'شركة التقدم للتجهيزات',
            'مؤسسة السلامة للمعدات',
            'شركة الرائد للتوزيع',
            'مؤسسة النجاح للتوريدات'
        ]
        
        suppliers = []
        for name in supplier_names:
            supplier, created = Supplier.objects.get_or_create(name=name)
            suppliers.append(supplier)
            if created:
                self.stdout.write(f'تم إنشاء مورد: {name}')
        
        # تأكد من وجود وحدات
        self.stdout.write('التحقق من وجود الوحدات...')
        from django.core.management import call_command
        call_command('create_units')
        
        # إنشاء المنتجات
        product_data = [
            {
                'name': 'جهاز حاسب مكتبي HP',
                'barcode': 'PC1001',
                'unit_code': 'device',
                'sender_name': 'محمد أحمد'
            },
            {
                'name': 'طابعة ليزر Canon',
                'barcode': 'PR2002',
                'unit_code': 'device',
                'sender_name': 'سعيد محمد'
            },
            {
                'name': 'شاشة عرض Samsung',
                'barcode': 'MN3003',
                'unit_code': 'device',
                'sender_name': 'فهد العلي'
            },
            {
                'name': 'لوحة مفاتيح Logitech',
                'barcode': 'KB4004',
                'unit_code': 'piece',
                'sender_name': 'خالد عبدالله'
            },
            {
                'name': 'فأرة لاسلكية Microsoft',
                'barcode': 'MS5005',
                'unit_code': 'piece',
                'sender_name': 'أحمد سالم'
            },
            {
                'name': 'سماعات رأس JBL',
                'barcode': 'HP6006',
                'unit_code': 'piece',
                'sender_name': 'عمر محمد'
            },
            {
                'name': 'قرص تخزين خارجي WD',
                'barcode': 'HD7007',
                'unit_code': 'piece',
                'sender_name': 'ناصر علي'
            },
            {
                'name': 'مكبرات صوت Bose',
                'barcode': 'SP8008',
                'unit_code': 'piece',
                'sender_name': 'سلمان حسين'
            },
            {
                'name': 'جهاز عرض Epson',
                'barcode': 'PJ9009',
                'unit_code': 'device',
                'sender_name': 'محمد عبدالرحمن'
            },
            {
                'name': 'راوتر لاسلكي TP-Link',
                'barcode': 'RT1010',
                'unit_code': 'device',
                'sender_name': 'فيصل سعد'
            }
        ]
        
        for data in product_data:
            supplier = random.choice(suppliers)
            try:
                # الحصول على الوحدة المناسبة
                try:
                    unit = Unit.objects.get(code=data['unit_code'])
                except Unit.DoesNotExist:
                    self.stdout.write(f'لم يتم العثور على الوحدة برمز {data["unit_code"]}، جاري إنشاؤها...')
                    unit = Unit.objects.create(
                        name=data['unit_code'].capitalize(),
                        code=data['unit_code']
                    )
                
                # إنشاء المنتج
                # إنشاء أحجام عبوة عشوائية
                package_sizes = [
                    "20-24-36", "18-22-30", "15-20-25", "12-16-24", "25-30-40", 
                    "10-15-20", "22-26-32", "14-18-22", None
                ]
                
                product, created = Product.objects.get_or_create(
                    barcode=data['barcode'],
                    defaults={
                        'name': data['name'],
                        'unit': unit,
                        'package_size': random.choice(package_sizes),
                        'sender_name': data['sender_name'],
                        'supplier': supplier
                    }
                )
                if created:
                    self.stdout.write(f'تم إنشاء منتج: {data["name"]}')
            except Exception as e:
                self.stdout.write(f'خطأ في إنشاء منتج {data["name"]}: {str(e)}')
        
        # إنشاء مطابقات الموردين
        for supplier in suppliers[:5]:  # نشئ مطابقات لأول 5 موردين فقط
            matching_file_name = f'مطابقة {supplier.name}'
            debt_amount = random.uniform(5000, 100000)
            payment_amount = debt_amount * random.uniform(0.1, 0.9) if random.random() > 0.3 else 0
            status_choices = ['complete', 'partial', 'pending']
            weights = [0.3, 0.4, 0.3]
            status = random.choices(status_choices, weights=weights, k=1)[0]
            
            matching, created = SupplierMatching.objects.get_or_create(
                supplier=supplier,
                matching_file_name=matching_file_name,
                defaults={
                    'matching_file': f'matching_files/supplier_{supplier.id}_matching.pdf',
                    'accountant_name': random.choice(['أحمد محمود', 'سامي خالد', 'فارس العلي', 'مازن سعيد']),
                    'debt_amount': debt_amount,
                    'payment_amount': payment_amount,
                    'status': status
                }
            )
            
            if created:
                self.stdout.write(f'تم إنشاء مطابقة للمورد: {supplier.name}')
        
        self.stdout.write(self.style.SUCCESS('تم إنشاء البيانات التجريبية بنجاح!'))
