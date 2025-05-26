-- إعادة تعيين قاعدة البيانات وإصلاح الترحيلات
-- حذف الجداول القديمة
DROP TABLE IF EXISTS stitec_product;
DROP TABLE IF EXISTS stitec_suppliermatching;
DROP TABLE IF EXISTS stitec_supplier;
DROP TABLE IF EXISTS stitec_unit;

-- إعادة تعيين حالة الترحيلات
DELETE FROM django_migrations WHERE app = 'stitec';
