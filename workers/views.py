from django.shortcuts import render
from .models import Worker

def worker_list(request):
    workers = Worker.objects.all()
    return render(request, 'workers/worker_list.html', {'workers':workers})

