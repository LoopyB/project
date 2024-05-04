from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('workers/', include('workers.urls')),
    path('', lambda request: redirect('workers/', permanent=False)),
]
