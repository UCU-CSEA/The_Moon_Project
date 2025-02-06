from django.shortcuts import render, get_object_or_404
from Moonrocks.models import Cadets

# Create your views here.
def card(request, id):
    # Get the cadet with the provided ID or return a 404 error if not found
    cadet = get_object_or_404(Cadets, id=id)

    # Check the gender of the cadet and select the appropriate template
    template_name = 'cards/m_card.html'  # Default to m_card.html
    if cadet.Gender == 'Female':  # Assuming the gender is stored as 'female' for female cadets
        template_name = 'cards/f_card.html'  # Use f_card.html for female cadets

    # Pass the cadet data to the context
    context = {
        'cadet': cadet,  # The entire cadet object
        'occupation': cadet.Occupation,  # Cadet's occupation
        'Names': cadet.Names,  # Cadet's name
    }

    # Render the appropriate template
    return render(request, template_name, context)