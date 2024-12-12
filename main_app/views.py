from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

# Create your views here.

# Classes
class Home(LoginView):
  template_name = 'home.html'

class About(TemplateView):
  template_name = 'about.html'

# Functions

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