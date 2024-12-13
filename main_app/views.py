from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TrackingFrom
from .models import Mushroom

from django.http import HttpResponse

# Create your views here.

# Classes
class Home(LoginView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'

class CreateMushroom(LoginRequiredMixin, CreateView):
  model = Mushroom
  fields = '__all__'

class MushroomUpdate(LoginRequiredMixin, UpdateView):
  model = Mushroom
  fields = '__all__'

class MushroomDelete(LoginRequiredMixin, DeleteView):
  model = Mushroom
  success_url = '/mushrooms/'

# Functions
def mushroom_index(request):
  mushrooms = Mushroom.objects.all()
  return render(request, 'mushrooms/index.html', {'mushrooms': mushrooms})

def mushroom_detail(request, mushroom_id):
  mushroom = Mushroom.objects.get(id=mushroom_id)
  traking_form = TrackingFrom()
  return render(request, 'mushrooms/detail.html', {
    'mushroom': mushroom,
    'tracking_form': traking_form
  })
  # return render(request, 'mushrooms/detail.html')

def record_mushroom(request, mushroom_id):
  form = TrackingFrom(request.POST)
  if form.is_valid():
    new_tracking = form.save(commit=False)
    new_tracking.mushroom_id = mushroom_id
  return redirect('home', mushroom_id=mushroom_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid Sign Up - Try Again'
  form = UserCreationForm()
  context = {
    'form': form,
    'error_message': error_message
  }
  return render(request, 'signup.html', context)