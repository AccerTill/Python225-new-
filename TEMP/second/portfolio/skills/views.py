from django.shortcuts import render
from .models import Skills

# Create your views here.

def index(request):
    projects = Skills.objects.all()
    return render(request, 'part_2/index.html', {'projects': projects})
