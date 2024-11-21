from django.shortcuts import render

# Create your views here.

def rocks(request):
    return render(request, 'Moonrocks/themoon.html')
