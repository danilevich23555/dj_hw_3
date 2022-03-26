from django.shortcuts import render, redirect
from django.http import HttpResponse
from phones.models import Phone

def index(request):
    return redirect('catalog')


def custom_key(people):
    return people[1]


def show_catalog(request):
    sort = request.GET.get('sort')
    phone_objects = Phone.objects.all()
    print(phone_objects)
    if sort == 'name':
        phone_objects = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
    template = 'catalog.html'
    context = {
        'phones': phone_objects,
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_objects = Phone.objects.all()
    for c in phone_objects:
        if c.slug == slug:
            result_phone = c
            break
    template = 'product.html'
    context = {
        'phone': result_phone
    }
    return render(request, template, context)


def list_phone(request):
    phone_objects = Phone.objects.all()
    phone = [f'{c.name}, {c.price}' for c in phone_objects]
    return  HttpResponse('<br>'.join(phone))