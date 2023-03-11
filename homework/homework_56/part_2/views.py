from django.shortcuts import render
from .models import Part_2
# Create your views here.

def index(request):
    projects = Part_2.objects.all()
    return render(request, 'part_2/index.html',
                  {"projects": projects})







