from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Member, Enquiry


# Create your views here.
def home(request):
    return render(request, "index.html", {'tab': 'home'})


def shop(request):
    return render(request, "shop.html", {'tab': 'shop'})


def about(request):
    return render(request, 'about.html', {'tab': 'about'})


def services(request):
    return render(request, 'services.html', {'tab': 'services'})


def contact(request):

    return render(request, 'contact.html', {'tab': 'contact'})


def blog(request):
    return render(request, 'blog.html', {'tab': 'blog'})


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def thankyou(request):
    return render(request, 'thankyou.html')


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        member = Member(name=name, email=email)
        member.save()
        messages.success(request, "You have subcribed successfully")
        return redirect("assets:cart")


def enquiry(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')

        msg = Enquiry(firstname=firstname, lastname=lastname, email=email, message=message)
        msg.save()
        messages.success(request, 'Message sent Successfully')
        return redirect("assets:home")
