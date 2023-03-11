from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

#  в Django все HTML окументы хранятся в папке templates

# #1
# def home(request):
#     return HttpResponse("Hello...")

#2
# def home(request):
#     return render(request, 'generator/home.html',
#                   {'password':'7erhf48f7$'})


def home(request):
    lst = list(range(6,15))
    return render(request, 'generator/home.html', {'lst':lst})

def password(request):
    char =[chr(i) for i in range(97,123)]


#UPPERCASE
    if request.GET.get('uppercase'):
        char.extend([chr(i) for i in range(65, 91)])

# NUMBERS
    if request.GET.get('numbers'):
        char.extend([chr(i) for i in range(48, 58)])

# SYMBOLS
    if request.GET.get('special'):
        char.extend([chr(i) for i in range(33, 48)])

# # To password page
#     if request.GET.get('lll'):
#         render(request, 'generator/password.html')

    length = int(request.GET.get('length')) # - обращение к элементу
    psw = ''
    for i in range(length):
        psw +=random.choice(char)
    return render(request, 'generator/password.html',
                  {'password':psw})

def about(request):
    return render(request, 'generator/about.html')

def password_back(request):
    return render(request, 'generator/password.html')

def single(request):
    aa=88
    return render(request, 'generator/single.html', {'aa':aa})