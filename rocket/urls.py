from django.urls import path
from . import views


urlpatterns = [
    path('',views.launch, name="page.launch"), #Form 
]