# دليل نشر المشروع على منصة Render

## الخطوات العامة

1. قم بإنشاء حساب على [Render](https://render.com/) إذا لم يكن لديك حساب بالفعل.
2. قم بتوصيل حسابك على Render بحساب GitHub أو GitLab الخاص بك.
3. أنشئ خدمة Web Service جديدة.

## إعداد متغيرات البيئة

بعد إنشاء الخدمة، قم بإعداد متغيرات البيئة التالية في لوحة تحكم Render تحت "Environment Variables":

### متغيرات قاعدة البيانات
- `DB_NAME`: اسم قاعدة البيانات
- `DB_USER`: اسم مستخدم قاعدة البيانات
- `DB_PASSWORD`: كلمة مرور قاعدة البيانات
- `DB_HOST`: عنوان مضيف قاعدة البيانات
- `DB_PORT`: منفذ قاعدة البيانات (عادةً 3306 لـ MySQL)

### متغيرات أساسية أخرى
- `SECRET_KEY`: مفتاح التشفير السري للتطبيق
- `DEBUG`: اضبطه على False للإنتاج
- `ALLOWED_HOSTS`: قائمة بالمضيفين المسموح لهم بالوصول، مثل `your-app-name.onrender.com`

## إعداد قاعدة البيانات

يمكنك استخدام أحد الخيارات التالية:

1. **قاعدة بيانات مستضافة على Render**:
   - أنشئ خدمة قاعدة بيانات MySQL من لوحة تحكم Render
   - استخدم بيانات الاتصال التي تقدمها Render في متغيرات البيئة

2. **قاعدة بيانات خارجية**:
   - استخدم خدمة مثل PlanetScale أو AWS RDS أو Azure Database
   - تأكد من أن قاعدة البيانات يمكن الوصول إليها من خادم Render

## إعدادات Build

في لوحة تحكم Render، قم بتحديد:

- **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
- **Start Command**: `gunicorn dataentery.wsgi --log-file -`

## هجرة قاعدة البيانات

بعد النشر الأول، ستحتاج إلى تشغيل هجرة قاعدة البيانات. يمكنك القيام بذلك من خلال:

```bash
python manage.py migrate
```

يمكنك تشغيل هذا الأمر من خلال Shell في لوحة تحكم Render.

## ملاحظات إضافية

- تأكد من أن ملف `Procfile` يحتوي على الإعداد الصحيح: `web: gunicorn dataentery.wsgi --log-file -`
- تأكد من وجود إصدار Python المناسب في ملف `runtime.txt`
- قم بتكوين CORS بشكل صحيح إذا كنت تستخدم واجهة برمجة تطبيقات REST
