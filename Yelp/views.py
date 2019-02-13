

from django.shortcuts import render
from .models import Food

def pizza(request):
    foods = Food.objects
    return render(request, 'pizza.html', {'foods':foods})
