from dataclasses import field, fields
from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from .models import Bird
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    return render(request, 'birds/bird_details.html', {'bird': bird})

class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'
    success_url = '/birds/'

class BirdUpdate(UpdateView):
    model = Bird
    fields = ('name', 'species', 'description', 'age')
    success_url = '/birds/'

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'