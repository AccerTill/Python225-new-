from django.shortcuts import render
from .models import Skills

# Create your views here.

def index(request):

    projects = Skills.objects.all() # данные из базы данных
    return render(request, 'skills/index.html',{'projects': projects})














