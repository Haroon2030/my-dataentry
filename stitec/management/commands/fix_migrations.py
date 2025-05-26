from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'إصلاح مشكلات الهجرات باستخدام SQL مباشر'

    def handle(self, *args, **kwargs):
        from django.db import connection
        
        self.stdout.write('جاري بدء إصلاح مشكلات الهجرة...')
        
        with connection.cursor() as cursor:
            # حذف جميع الجداول المتعلقة بالتطبيق
            self.stdout.write('حذف الجداول القديمة...')
            try:
                cursor.execute("DROP TABLE IF EXISTS stitec_product")
                cursor.execute("DROP TABLE IF EXISTS stitec_suppliermatching")
                cursor.execute("DROP TABLE IF EXISTS stitec_supplier")
                cursor.execute("DROP TABLE IF EXISTS stitec_unit")
            except Exception as e:
                self.stdout.write(f"خطأ في حذف الجداول: {str(e)}")
            
            # إعادة تعيين حالة الهجرات
            self.stdout.write('إعادة تعيين حالة الهجرات...')
            try:
                cursor.execute("DELETE FROM django_migrations WHERE app = 'stitec'")
            except Exception as e:
                self.stdout.write(f"خطأ في إعادة تعيين الهجرات: {str(e)}")
        
        self.stdout.write(self.style.SUCCESS('تم إصلاح مشكلات الهجرة بنجاح! قم بتطبيق الهجرات مرة أخرى باستخدام: python manage.py migrate'))
