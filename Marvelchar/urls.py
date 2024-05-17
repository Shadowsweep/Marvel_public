"""
URL configuration for Marvelchar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,re_path
from marvelcharactersapp import char_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',char_view.Index),
    re_path(r'^api/results',char_view.display_csv_data),
    re_path(r'^api/displaycsv',char_view.csv_display),
    re_path(r'^api/fightpage',char_view.start_area),
    re_path(r'^api/arenafight',char_view.FightArena),
   
]
