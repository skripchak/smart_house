from django.shortcuts import render
from .models import House, Outlet, Room
from django.http import HttpResponse, JsonResponse
import random


def main_page(request):
    context = {'houses': House.objects.all()}
    return render(request, 'main.html', context)


def house_page(request, id):
    house = House.objects.get(id=id)
    rooms = Room.objects.filter(house=house)
    outlets = Outlet.objects.filter(outlet__in=rooms)
    context = {'house': house, 'outlets': outlets}
    return render(request, 'house.html', context)


def house_choose_room(request, id):
    house = House.objects.get(id=id)
    rooms = house.room_set.all()
    return render(request, 'rooms.html', {'rooms': rooms, 'house': house})
