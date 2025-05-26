from django.core.management.base import BaseCommand
from stitec.models import Unit

class Command(BaseCommand):
    help = 'إنشاء وحدات افتراضية للنظام'

    def handle(self, *args, **kwargs):
        self.stdout.write('جاري إنشاء الوحدات الافتراضية...')
        
        # وحدات افتراضية
        default_units = [
            {'name': 'قطعة', 'code': 'piece'},
            {'name': 'جهاز', 'code': 'device'},
            {'name': 'صندوق', 'code': 'box'},
            {'name': 'كرتون', 'code': 'carton'},
            {'name': 'علبة', 'code': 'pack'},
            {'name': 'متر', 'code': 'meter'},
            {'name': 'كيلوغرام', 'code': 'kg'},
            {'name': 'لتر', 'code': 'liter'}
        ]
        
        for unit_data in default_units:
            unit, created = Unit.objects.get_or_create(
                code=unit_data['code'],
                defaults={'name': unit_data['name']}
            )
            
            if created:
                self.stdout.write(f'تم إنشاء وحدة: {unit.name}')
            else:
                self.stdout.write(f'الوحدة {unit.name} موجودة بالفعل')
        
        self.stdout.write(self.style.SUCCESS('تم إنشاء الوحدات الافتراضية بنجاح!'))
