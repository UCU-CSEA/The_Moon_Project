from django.shortcuts import render
from .models import Cadets

# Create your views here.

def rocks(request):
    cadets = Cadets.objects.all()
    template_data = {}
    template_data['title'] = 'The Moon'
    template_data['cadet'] =  cadets
    return render(request, 'Moonrocks/themoon.html', {'template_data':template_data})
