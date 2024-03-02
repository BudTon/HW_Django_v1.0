from django.shortcuts import render, redirect
# from phones.
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort == 'name':
        phones = sorted(Phone.objects.all(), key=lambda phone: phone.name)
    elif sort == 'min_price':
        phones = sorted(Phone.objects.all(), key=lambda phone: phone.price)
    elif sort == 'max_price':
        phones = sorted(Phone.objects.all(), key=lambda phone: phone.price, reverse=True)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    for phone_objects in Phone.objects.all():
        if phone_objects.slug == slug:
            phone_slug = phone_objects
    context = {'phone': phone_slug}
    return render(request, template, context)
