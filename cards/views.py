from django.shortcuts import render, get_object_or_404
from Moonrocks.models import Cadets
from datetime import date 

# Create your views here.
def card(request, id):
    # Get the cadet with the provided ID or return a 404 error if not found
    cadet = get_object_or_404(Cadets, id=id)


    location = {}


    location['coordinates'] = "9P4R+RG8, Mukono"
    location['name'] = 'Nkoyoyo Hall, UCU Main Campus'
    location['address'] = ' Bishop Tucker Rd'

    event = {}

    event['name'] = "HACK UCU 2025"
    event['date'] = date.today()

    # Pass the cadet data to the context
    context = {
        'cadet': cadet,  # The entire cadet object
        'Names': cadet.Names,  # Cadet's name
        'location': location,
        'event': event,
    }

    # Render the appropriate template
    return render(request, 'cards/m_card.html', context)