from django.shortcuts import render, redirect
# форма входа в личный кабинет
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def home(request):
    return render(request, 'todo/home.html')




# форма входа в личный кабинет
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html',
                      {'form': UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')  # ------------REDIRECTION

            except IntegrityError: # ------------- IMPORTED UPPER
                return render(request, 'todo/signupuser.html',
                              {'form': UserCreationForm(),
                               'error':'Такое имя пользователя уже '
                                       'существует. Задайте новое.'})

        else:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(),
                           'error':'Пароли не совпадают.'})





def loginuser(request):
    if request.method == "GET":
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        # если пользователя не существует
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': 'Неверные данные для входа'})
        else:
            login(request, user)
            return redirect('currenttodos')




def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')




def currenttodos(request):
    return render(request, 'todo/currenttodos.html')


# -----ФОРМА ОТПРАВЛЯЕТСЯ МЕТОДОМ POST !!!!








