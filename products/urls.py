from django.urls import path
import products.views

urlpatterns = [
    path('create', products.views.create, name='create'),
]
