from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages



def userLogin(request):

    if request.user.is_authenticated:
        return redirect('/')

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
            return redirect('/')
        else:
            messages.error(request, "Username or Password is incorrect")

    context = {
        
    }

    return render(request, 'dashboard/login.html', context)


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


def userLogout(request):
    logout(request)
    messages.error(request, 'Logged Out')
    return redirect('/')
