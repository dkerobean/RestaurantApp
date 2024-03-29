from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from .forms import FoodForm, FoodTypeForm, CategoryForm, ProfileForm, createUserForm
from .models import Food, Category, FoodType
from main.models import Contact, Reservation
from user.models import Profile


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
@permission_required("food.create_food", login_url="permission")
def createFood(request):
    
    form = FoodForm()
    
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food Added!')
            return redirect('addMenu')
            
    
    context = {
        'form':form
    }
    
    return render(request, 'dashboard/createFood.html', context)


@login_required(login_url="login")
@permission_required("food.delete_food", login_url="permission")
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


@login_required(login_url="login")
@permission_required("food.update_food", login_url="permission")
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
@permission_required("food.view_food", login_url="permission")
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


@login_required(login_url="login")
@permission_required("contact.view_contact", login_url="permission")
def contact(request):
    
    message = Contact.objects.all()
    
    context = {
        'message':message
    }
    
    return render(request, 'dashboard/contact.html',context)


@login_required(login_url="login")
def reservation(request):
    
    reservation = Reservation.objects.all()

    context = {
        'reservation':reservation
    }

    return render(request, 'dashboard/reservation.html', context)


@login_required(login_url="login")
@permission_required("contact.delete_contact", login_url="permission")
def deleteContact(request, pk):

    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Message Deleted Successfully')
        return redirect('messages')

    context = {
        'object': contact
    }

    return render(request, 'dashboard/delete.html', context)


@login_required(login_url="login")
@permission_required("reservation.delete_reservation", login_url="permission")
def deleteReservation(request, pk):

    reservation = Reservation.objects.get(id=pk)

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Message Deleted Successfully')
        return redirect('reservations')

    context = {
        'object': reservation
    }

    return render(request, 'dashboard/delete.html', context)


@login_required(login_url="login")
@permission_required("category.create_category", login_url="permission")
def createCategory(request):
    
    form = CategoryForm()
    categories = Category.objects.all()

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category Added!')
            return redirect('categories')

    context = {
        'form': form,
        'categories':categories
    }

    return render(request, 'dashboard/categories.html', context)


@login_required(login_url="login")
@permission_required("category.delete_category", login_url="permission")
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)

    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Message Deleted Successfully')
        return redirect('categories')

    context = {
        'object': category
    }

    return render(request, 'dashboard/delete.html', context)


@login_required(login_url="login")
@permission_required("foodtype.create_foodtype", login_url="permission")
def createFoodtype(request):

    form = FoodTypeForm()
    foodtypes = FoodType.objects.all()

    if request.method == "POST":
        form = FoodTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'FoodType Added!')
            return redirect('foodtype')

    context = {
        'form': form,
        'foodtypes': foodtypes
    }

    return render(request, 'dashboard/foodtype.html', context)


@login_required(login_url="login")
@permission_required("foodtype.delete_foodtype", login_url="permission")
def deleteFoodtype(request,pk):
    foodtype = FoodType.objects.get(id=pk)

    if request.method == 'POST':
        foodtype.delete()
        messages.success(request, 'FoodType Deleted Successfully')
        return redirect('foodtype')

    context = {
        'object': foodtype
    }

    return render(request, 'dashboard/delete.html', context)


@login_required(login_url="login")
def viewProfile(request, pk):
    
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user = user)
    
    form = ProfileForm(instance=profile)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user = form.save(commit=False)
            user.user =  request.user
            user.save()
            messages.success(request, 'Profile Edited')
            return redirect('profile', pk=request.user.id)
    
    
    context ={
        'form':form, 
        'user':user, 
        'profile':profile
    }
    
    
    return render(request, 'dashboard/profile.html', context)


@login_required(login_url="login")
@permission_required("user.add_user", login_url="permission")
def createUser(request):
    
    form = createUserForm()
    
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Created')
            return redirect('createUser')
    
    context = {
        'form':form
    }
    
    
    return render(request, 'dashboard/addUser.html', context)


@login_required(login_url="login")
@permission_required("user.view_user")
def viewUsers(request):
    
    users = User.objects.all()
    
    context = {
        'users':users
    }
    
    return render(request, 'dashboard/viewUsers.html', context)


@login_required(login_url="login")
@permission_required("user.delete_user")
def deleteUsers(request, pk):

    users = User.objects.get(id=pk)
    
    if request.method == 'POST':
        users.delete()
        messages.success(request, 'User Deleted Successfully')
        return redirect('viewUsers')
    
    

    context = {
        'object': users
    }

    return render(request, 'dashboard/delete.html', context)


def permissionEror(request):
    
    return render(request, 'dashboard/permission.html')


    
