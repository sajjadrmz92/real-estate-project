from django.shortcuts import render
from .models import Property

def property_list(request):
    # دریافت املاک فعال
    properties = Property.objects.filter(is_active=True)
    return render(request, 'properties/property_list.html', {'properties': properties})