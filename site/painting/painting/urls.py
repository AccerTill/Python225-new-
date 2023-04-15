"""painting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  #  standart for showing images:
from django.conf import settings
from sorting import views  #  for HTML pages:
from team import views as views_team


urlpatterns = [
    path('admin/', admin.site.urls),
    # ----for HTML pages:
    path('', views.index, name = 'index'),
    path('blog/', include('blog.urls')),
    path('about/', views.about, name='about'),
    # для регистрации:
    path('signup/', views_team.signupuser, name = 'signupuser'),
    path('logout',views_team.logoutuser, name = 'logoutuser'),
    path('login/', views_team.loginuser, name = 'loginuser'),
    

    # для задач:
    path('', views_team.home, name ='home'),
    path('current/', views_team.currentteam, name ='currentteam'),
    path('create/', views_team.createteam, name='createteam'),
    path('team/<int:team_pk>', views_team.viewteam, name ='viewteam'),
    path('team/<int:team_pk>/complete>', views_team.completeteam, name ='completeteam'),
    path('team/<int:team_pk>/delete>', views_team.deleteteam, name='deleteteam'),
    path('completed/', views_team.completedteam, name='completedteam'),
]



urlpatterns +=static(settings.MEDIA_URL,
                     document_root=settings.MEDIA_ROOT)












