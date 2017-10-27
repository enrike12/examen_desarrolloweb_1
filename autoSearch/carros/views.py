# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView

from .models import Car


# Create your views here.
def home(request):
    return render(request, "home.html")


class car_list(ListView):
    template_name='car_list.html'
    queryset=Car.objects.all()

class car_detail(DetailView):
    template_name='car_detail.html'
    queryset= Car.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Car.objects.get(id=id)
