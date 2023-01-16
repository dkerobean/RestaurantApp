from django.shortcuts import render
from django.contrib import messages




def reservation(request):
    
    context = {
        
    }
    
    return render(request, 'user/reservation.html', context)



def contact(request):
    
    context = {
        
    }
    
    return render(request, 'user/contact.html', context)



