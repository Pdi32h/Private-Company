from django.shortcuts import render
from .models import Home, Contact, Standard, About, Product, Gallery, Wallpaper
from django.views import View


def home(request):
    homes = Home.objects.all()
    standard = Standard.objects.all()
    return render(request, 'home/home.html', {'home': homes, 'standard': standard})


def product(request):
    wallpapers = Wallpaper.objects.all()
    homes = Home.objects.all()
    products = Product.objects.all()
    return render(request, 'home/product.html',
                  {'products': products, 'home': homes, 'wallpapers': wallpapers})


def gallery(request):
    wallpapers = Wallpaper.objects.all()
    album = Gallery.objects.all()
    homes = Home.objects.all()
    standard = Standard.objects.all()
    return render(request, 'home/gallery.html',
                  {'gallery': album, 'standard': standard, 'home': homes, 'wallpapers': wallpapers})


def contact(request):
    homes = Home.objects.all()
    about = About.objects.all()
    if request.method == 'POST':
        contacts = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contacts.name = name
        contacts.email = email
        contacts.phone = phone
        contacts.message = message
        contacts.save()
        return render(request, 'home/contact.html', {'home': homes, 'about': about})
    else:
        return render(request, 'home/contact.html', {'home': homes, 'about': about})


def handler404(request, exception):
    return render(request, '404.html', status=404)
