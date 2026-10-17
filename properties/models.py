from django.db import models

class Property(models.Model):
    # نوع معامله (فروش یا رهن و اجاره)
    TRANSACTION_TYPES = (
        ('sale', 'فروش'),
        ('rent', 'رهن و اجاره'),
    )

    # نوع ملک
    PROPERTY_TYPES = (
        ('apartment', 'آپارتمان'),
        ('house', 'ویلایی / خانه'),
        ('land', 'زمین / کلنگی'),
        ('commercial', 'تجاری / اداری'),
    )

    title = models.CharField(max_length=200, verbose_name="عنوان آگهی")
    description = models.TextField(verbose_name="توضیحات کامل")
    
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, verbose_name="نوع معامله")
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPES, verbose_name="نوع ملک")
    
    price = models.DecimalField(max_length=15, max_digits=15, decimal_places=0, verbose_name="قیمت (تومان)")
    area = models.PositiveIntegerField(verbose_name="متراژ (مترمربع)")
    bedrooms = models.PositiveSmallIntegerField(default=1, verbose_name="تعداد اتاق خواب")
    
    city = models.CharField(max_length=100, verbose_name="شهر")
    address = models.CharField(max_length=255, verbose_name="آدرس دقیق یا محدوده")
    
    is_active = models.BooleanField(default=True, verbose_name="فعال / منتشر شده")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ بروزرسانی")

    image = models.ImageField(upload_to='properties/', blank=True, null=True, verbose_name="تصویر اصلی ملک")

    def __str__(self):
        return f"{self.title} - {self.get_transaction_type_display()}"

    class Meta:
        verbose_name = "ملک"
        verbose_name_plural = "املاک"
        ordering = ['-created_at']