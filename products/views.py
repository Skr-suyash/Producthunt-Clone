from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

def home(request):

    return render(request, 'products/home.html')

@ login_required
def create(request):

    if request.method == 'POST':
        product = Product()
        product.title = request.POST['title']
        product.description = request.POST['description']
        product.url = request.POST['url']
        product.icon = request.FILES['icon']
        product.image = request.FILES['image']
        product.pub_date = timezone.datetime.now()
        product.hunter = request.user

        product.save()
        
        return redirect('home')

    return render(request, 'products/create.html')