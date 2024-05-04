from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workers/', include('workers.urls')),
    path('', lambda request: redirect('workers/', permanent=False)),
    #path('worker/<int:pk>/edit/', views.worker_edit, name='worker_edit'),
    #path('worker/<int:pk>/delete/', views.worker_delete, name='worker_delete'),
]
