import mysql.connector

# اتصال بقاعدة البيانات
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="52640",
    database="data_db"
)

# إنشاء كيرسر
cursor = conn.cursor()

print("جاري إصلاح مشكلات الترحيلات...")

try:
    # حذف جميع الجداول المتعلقة بالتطبيق
    print("حذف الجداول القديمة...")
    cursor.execute("DROP TABLE IF EXISTS stitec_product")
    cursor.execute("DROP TABLE IF EXISTS stitec_suppliermatching")
    cursor.execute("DROP TABLE IF EXISTS stitec_supplier")
    cursor.execute("DROP TABLE IF EXISTS stitec_unit")
    
    # إعادة تعيين حالة الهجرات
    print("إعادة تعيين حالة الترحيلات...")
    cursor.execute("DELETE FROM django_migrations WHERE app = 'stitec'")
    
    # تأكيد التغييرات
    conn.commit()
    print("تم إصلاح مشكلات الترحيلات بنجاح!")
    
except Exception as e:
    print(f"حدث خطأ: {str(e)}")
    conn.rollback()

finally:
    # إغلاق الاتصال
    cursor.close()
    conn.close()

print("الآن يمكنك تطبيق الترحيلات مرة أخرى باستخدام: python manage.py migrate")
