from django.shortcuts import render, get_object_or_404
from .models import Food

def pizza(request):
    foods = Food.objects
    return render(request, 'pizza.html', {'foods':foods})

def detail(request, food_id):
    food_detail = get_object_or_404(Food, pk=food_id)
    return render(request, 'detail.html', {'food':food_detail})
