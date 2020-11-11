from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def testimonial(request):
    return render(request, 'testimonial.html', {})

def team(request):
    return render(request, 'team.html', {})

def views(request):
    return render(request, 'views.html', {})

def contact(request):
    return render(request, 'contact.html', {})

@login_required(login_url='redirect_to_login')
def download(request):
    return render(request, 'download.html', {})