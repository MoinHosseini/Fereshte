from django.shortcuts import render
from .models import Item
from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.

from django.db.models import Count

class ItemListView(ListView):
    model = Item  
    template_name = 'item_list.html'  
    context_object_name = 'items_by_category'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items_by_category = []
        
        # Get distinct categories
        categories = Item.objects.values_list('category__name', flat=True).distinct()
        
        # Query items grouping by category 
        for category in categories:
            items = Item.objects.filter(category__name=category)
            items_by_category.append({
                'name': category, 
                'items': items
            })

        context['items_by_category'] = items_by_category
        return context