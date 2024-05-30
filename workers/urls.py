from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_list, name='worker_list'),
    path('worker/new/', views.worker_new, name='worker_new'),
    path('worker/<int:pk>/edit/', views.worker_edit, name='worker_edit'),
    path('worker/<int:pk>/delete/', views.worker_delete, name='worker_delete'),
]