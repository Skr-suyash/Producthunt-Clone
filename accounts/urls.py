from django.urls import path
import accounts.views

urlpatterns = [
    path('login', accounts.views.login, name='login'),
    path('signup', accounts.views.signup, name='signup'),
    path('logout', accounts.views.logout, name='logout'),
]
