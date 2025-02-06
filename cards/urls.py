from django.urls import path
from . import views


urlpatterns = [
    
    #path('',views.card, name="cards.card"), #Form 
    path('<int:id>/',views.card, name='cards.card'),
    
]