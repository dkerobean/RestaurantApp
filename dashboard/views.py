from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import FoodForm, FoodTypeForm, CategoryForm
from .models import Food


def userLogin(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect('dashboard')
        else:
            messages.error(request, "Username or Password is incorrect")

    context = {

    }

    return render(request, 'dashboard/index.html', context)


# def userRegister(request):

#     form = CustomUserCreationForm()
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.save()

#             login(request, user)
#             messages.success(request, "User Created")
#             return redirect('/')

#     context = {
#         'form': form
#     }

#     return render(request, 'user/login_register.html', context)

@login_required(login_url="login")
def userLogout(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def dashbord(request):
    
    context = {
        
    }
    
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url="login")
def createFood(request):
    
    form = FoodForm()
    
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food Added!')
            return redirect('dashboard')
            
    
    context = {
        'form':form
    }
    
    return render(request, 'dashboard/createFood.html', context)


@login_required(login_url="login")
def deleteFood(request,pk):
    
    food = Food.objects.get(id=pk)
    
    if request.method == 'POST':
        food.delete()
        messages.success(request, 'Food Deleted Successfully')
        return redirect('viewMenu')
    
    
    context = {
        'object':food
    }
    
    return render(request, 'dashboard/delete.html', context)


def updateFood(request,pk):
    
    food = Food.objects.get(id=pk)
    
    form = FoodForm(instance=food)
    
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfuly')
            return redirect('viewMenu')
    
    context = {
        'form':form
    }
    
    
    return render(request, 'dashboard/updateFood.html', context)


@login_required(login_url="login")
def viewMenu(request):
    
    foods = Food.objects.all()
    
    context = {
        'foods':foods
    }

    return render(request, 'dashboard/menuList.html', context)


@login_required(login_url="login")
def foodDetail(request, pk):
    
    food = Food.objects.get(id=pk)
    
    context = {
        'food':food
    }
    
    return render(request, 'dashboard/foodDetail.html', context)