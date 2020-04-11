from django.urls import path
import products.views

urlpatterns = [
    path('create', products.views.create, name='create'),
    path('<int:product_id>', products.views.detail, name='detail'),
    path('<int:product_id>/upvote', products.views.upvote, name='upvote')
]
