from django.shortcuts import render
from .models import House, Outlet
from django.http import HttpResponse, JsonResponse
import random


def main_page(request):
    context = {'houses': House.objects.all()}

    return render(request, 'main.html', context=context)


def monitor(request):
    data = [

    ]

    houses = House.objects.all()

    for house in houses:
        for outlet in house.outlets.all():
            outlet.electricity_consumption = int(random.triangular(0, 3500, 100))
            data.append({
                'house': house.id,
                house.id: outlet.electricity_consumption
            })
            outlet.save()

    return JsonResponse(data, safe=False)
