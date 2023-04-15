from django.shortcuts import render
from .models import Sorting
# Create your views here.


# - Show page with pictures
def index(request):
    projects = Sorting.objects.all()
    return render(request, 'sorting/index.html', {'projects': projects})


def about(request):
    return render(request, 'sorting/about.html')





