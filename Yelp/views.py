from __future__ import unicode_literals
from django.views.generic import TemplateView

from django.shortcuts import render
from .models import Food

class PizzaView(TemplateView):
    template_name = 'pizza.html'

def pizza(request):
    Foods = Food.objects
    return render(request, 'yelp/pizza.html', {'Foods':Foods})
