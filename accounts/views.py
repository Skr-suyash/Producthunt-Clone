from django.shortcuts import render


def signup(request):

    return render(request, 'accounts/signup.html')


def login(request):

    return render(request, 'accounts/login.html')


def signout(request):

    return render(request, 'accounts/signout.html')

