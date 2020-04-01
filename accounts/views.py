from django.shortcuts import render, redirect
from django.contrib.auth.admin import User
from django.contrib import auth


def signup(request):

    if (request.method == 'POST'):
        # User wants an account now

        if (request.POST['password1'] == request.POST['password2']):

            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})

    else:       
        return render(request, 'accounts/signup.html')


def login(request):

    return render(request, 'accounts/login.html')


def signout(request):

    return render(request, 'accounts/signout.html')

