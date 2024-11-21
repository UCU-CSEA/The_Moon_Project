from django.shortcuts import render

# Create your views here.
def launch(request): #sign up form
    return render(request, 'rocket/launch.html')