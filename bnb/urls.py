from . import views
from django.urls import path
from .views import create_customer

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('contact/', views.Contact.as_view(), name='contact_us'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', create_customer, name='contact_us'),
    path('breakfast/', views.Breakfast.as_view(), name='breakfast'),
    # path('myaccount/', views.MyAccount.as_view(), name='my_account'),
]
