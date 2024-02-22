from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))

def write_csv():
    with open('data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
        dict_bus_stations = csv.DictReader(csvfile)
        list_bus_stations = [row for row in dict_bus_stations]
    return list_bus_stations

def bus_stations(request):
    list_bus_stations = write_csv()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(list_bus_stations, 20)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
