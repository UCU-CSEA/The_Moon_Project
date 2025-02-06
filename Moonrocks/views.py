from django.shortcuts import render, redirect
from .models import Cadets
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def rocks(request):
    cadets = Cadets.objects.all()
    template_data = {}
    template_data['title'] = 'The Moon'
    template_data['cadet'] =  cadets
    return render(request, 'Moonrocks/themoon.html', {'template_data':template_data})

@csrf_exempt
def addCadet(request):
     if request.method == 'POST' and request.POST['gender'] !='':
          cadets = Cadets()
          cadets.Names = request.POST['name']
          cadets.Gender = request.POST['gender']
          cadets.Organization = request.POST['organization']
          cadets.Occupation = request.POST['occupation']
          cadets.Quote = request.POST['quote']
          cadets.save()
          return redirect('Moonrocks.rocks')

