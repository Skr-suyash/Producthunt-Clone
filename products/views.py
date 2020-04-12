from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
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
        
        return redirect('/products/' + str(product.id))

    return render(request, 'products/create.html')


def detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/detail.html', {'product': product})


@ login_required
def upvote(request, product_id):

    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.total_votes += 1
        product.save()
        # return redirect('/products/' + str(product_id))
        return HttpResponse()

