from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Contact

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def product(request):
    return render(request, 'product.html', {})

def testimonial(request):
    return render(request, 'testimonial.html', {})

def team(request):
    return render(request, 'team.html', {})

def views(request):
    return render(request, 'views.html', {})

def contact(request):
    if request.method == "POST":
        email = request.POST['email']
        title = request.POST['title']
        text = request.POST['text']

        new_contact = Contact()
        new_contact.email = email
        new_contact.title = title
        new_contact.text = text
        new_contact.save()

        messages.success(request, 'Thank you for contacting us! We will get back to you soon!')

    return render(request, 'contact.html', {})

@login_required(login_url='redirect_to_login')
def download(request):
    return render(request, 'download.html', {})
