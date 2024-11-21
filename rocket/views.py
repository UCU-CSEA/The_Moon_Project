from django.shortcuts import render


#sign up form
def launch(request): 
    return render(request, 'rocket/launch.html')

#add to database from form 

