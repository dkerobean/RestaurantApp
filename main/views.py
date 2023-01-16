from django.shortcuts import render,redirect
from .forms import ContactForm, ReservationForm
from django.contrib import messages

def home(request):
    context = {
        
    }
    return render(request, 'main/index.html', context)



def contact(request):
    
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent')
            return redirect('contact')
    
    context = {
        'form':form
    }
    
    return render(request, 'main/contact.html', context)


def about(request):
    
    context = {
        
    }
 
    return render(request, 'main/about.html', context)


def menu(request):
    context = {
        
    }
    
    return render(request, 'main/menu.html', context)

    

def reservation(request):
    
    form = ReservationForm()
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Table Reserved')
            return redirect('reservation')
        

    context = {
        'form': form
    }

    

    return render(request, 'main/reservation.html',context)
