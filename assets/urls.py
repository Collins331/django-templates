from django.urls import path
from . import views

app_name = 'assets'
urlpatterns = [
    path('', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('enquiry', views.enquiry, name='enquiry'),
]
