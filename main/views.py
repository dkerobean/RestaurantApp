from django.shortcuts import render

def home(request):
    context = {
        
    }
    return render(request, 'main/index.html', context)



def contact(request):
    
    context={
        
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