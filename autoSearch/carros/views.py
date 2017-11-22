# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .forms import CarModelForm
from .models import Car
from .mixin import FormUserNeededMixin


# Create your views here.
def home(request):
    car = Car.objects.all()
    return render(request, "home.html", context= {"msg": "hola ", "car":car})

class CarCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = CarModelForm
    template_name = "car/create_view.html"
    success_url = "/car/list"
    login_url = "/admin"

class CarUpdateView(UpdateView):
    queryset = Car.objects.all()
    form_class = CarModelForm
    template_name = "car/carupdate_view.html"
    success_url = "/car/list"

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = "car/CarDeleteView.html"
    success_url = reverse_lazy("CarList")

class CarDetailView(DetailView):
    template_name = "car/detail.html"
    queryset = Car.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        print id
        return Car.objects.get(id=id)


class CarListView(ListView):
    template_name = "car/car_list.html"
    #queryset=Car.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Car.objects.all()
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                            Q(make__icontains=query) |
                            Q(types__icontains=query)
                          )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(CarListView, self).get_context_data(*args, **kwargs)
        print context
        context['create_form'] = CarModelForm()
        context['create_url'] = reverse_lazy("CarCreate")
        return context
