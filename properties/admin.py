from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'transaction_type', 'property_type', 'price', 'city', 'is_active', 'created_at')
    list_filter = ('transaction_type', 'property_type', 'is_active', 'city')
    search_fields = ('title', 'description', 'address', 'city')
    list_editable = ('is_active',)