from dataclasses import field, fields
from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from .models import Bird, Feeding, Toy
from .forms import FeedingForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from main_app import models

# Create your views here.

def home_page(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def get_bird_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})


def get_bird_details(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    feeding_form = FeedingForm()
    return render(request, 'birds/bird_details.html', {
        'bird': bird,
        'feeding_form': feeding_form,
        })


def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('details', bird_id=bird_id)


class BirdCreate(CreateView):
    model = Bird
    fields = ('name', 'species', 'description', 'age')
    success_url = '/birds/'


class BirdUpdate(UpdateView):
    model = Bird
    fields = ('name', 'species', 'description', 'age')
    success_url = '/birds/'


class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'


class ToyCreate(CreateView):
    model = Toy
    fields = ('name', 'color')
    success_url = '/toys/'


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'


class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/details.html'


class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'


class ToyUpdate(UpdateView):
    model = Toy
    fields = ('name', 'color')
    success_url = '/toys/'
    