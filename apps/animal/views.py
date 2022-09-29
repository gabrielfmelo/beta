from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Animal

# Create your views here.


def home(request):
    return render(request, 'animal/home.html')

def about(request):
    return render(request, 'animal/about.html')

class AnimalCreateView(CreateView):
    model = Animal
    fields = '__all__' 
    success_url = reverse_lazy('animal:lista')

class AnimalListView(ListView):
    model = Animal
