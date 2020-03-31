from django.urls import path
import accounts.views

urlpatterns = [
    path('login', accounts.views.login, name='login'),
    path('signup', accounts.views.signup, name='signup'),
    path('signout', accounts.views.signout, name='signout'),
]
