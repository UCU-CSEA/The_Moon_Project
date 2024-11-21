from django.urls import path
from . import views

urlpatterns = [
    path('', views.rocks, name= 'Moonrocks.rocks')
]