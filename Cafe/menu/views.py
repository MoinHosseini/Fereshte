from django.shortcuts import render
from .models import Item
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.

from django.db.models import Count
from django.db.models import Q

class ItemListView(ListView):
    model = Item  
    template_name = 'item_list.html'  
    context_object_name = 'items_by_category'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items_by_category = []
        
        # Get distinct categories
        categories = Item.objects.values_list('category__name', flat=True).distinct()

        top_items = Item.objects.order_by('-likes')[:5]
        discounted_items = Item.objects.filter(Q(discount__gt=0))

        # Query items grouping by category 
        for category in categories:
            items = Item.objects.filter(category__name=category)
            items_by_category.append({
                'name': category, 
                'items': items
            })

        context['items_by_category'] = items_by_category
        context['top_items'] = top_items
        context['discounted_items'] = discounted_items
        
        return context


def update_reactions(request, id, type):
    item = Item.objects.get(id=id)
    if type == "like":
        item.likes += 1 
    else:
        item.dislikes += 1

    item.save()
    
    return redirect('list') # Redirect back