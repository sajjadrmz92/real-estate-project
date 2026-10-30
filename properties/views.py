from django.shortcuts import render, get_object_or_404
from .models import Property

def property_list(request):
    # فقط املاکی که فعال هستند را نمایش می‌دهیم
    properties = Property.objects.filter(is_active=True).order_by('-created_at')
    
    # فیلترها
    transaction_type = request.GET.get('transaction_type')
    property_type = request.GET.get('property_type')
    search_query = request.GET.get('q')

    if transaction_type:
        properties = properties.filter(transaction_type=transaction_type)
    if property_type:
        properties = properties.filter(property_type=property_type)
    if search_query:
        properties = properties.filter(title__icontains=search_query)

    context = {
        'properties': properties,
    }
    return render(request, 'properties/property_list.html', context)

def property_detail(request, pk):
    property_item = get_object_or_404(Property, pk=pk, is_active=True)
    
    context = {
        'property': property_item,
    }
    return render(request, 'properties/property_detail.html', context)