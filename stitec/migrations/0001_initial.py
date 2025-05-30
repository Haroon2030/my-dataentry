# Generated by Django 5.2 on 2025-05-21 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم المورد')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
            ],
            options={
                'verbose_name': 'المورد',
                'verbose_name_plural': 'الموردين',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='اسم الوحدة')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='رمز الوحدة')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
            ],
            options={
                'verbose_name': 'الوحدة',
                'verbose_name_plural': 'الوحدات',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SupplierMatching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matching_file_name', models.CharField(max_length=50, verbose_name='اسم ملف المطابقة')),
                ('matching_file', models.FileField(help_text='يمكن تحميل ملفات PDF أو Word', upload_to='matching_files/', verbose_name='ملف المطابقة')),
                ('accountant_name', models.CharField(max_length=255, verbose_name='اسم المحاسب')),
                ('debt_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='المديونية')),
                ('payment_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='السداد')),
                ('status', models.CharField(choices=[('complete', 'مكتمل'), ('partial', 'جزئي'), ('pending', 'معلق')], default='pending', max_length=20, verbose_name='الحالة')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchings', to='stitec.supplier', verbose_name='المورد')),
            ],
            options={
                'verbose_name': 'مطابقة المورد',
                'verbose_name_plural': 'مطابقات الموردين',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='اسم الصنف')),
                ('barcode', models.CharField(max_length=20, unique=True, verbose_name='الباركود')),
                ('package_tension', models.BooleanField(default=False, verbose_name='شد العبوة')),
                ('package_size', models.CharField(blank=True, help_text='مثال: 20-24-36', max_length=50, null=True, verbose_name='حجم العبوة')),
                ('sender_name', models.CharField(max_length=255, verbose_name='اسم المرسل')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stitec.supplier', verbose_name='المورد')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='stitec.unit', verbose_name='الوحدة')),
            ],
            options={
                'verbose_name': 'المنتج',
                'verbose_name_plural': 'المنتجات',
                'ordering': ['-created_at'],
            },
        ),
    ]
