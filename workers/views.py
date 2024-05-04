from django.shortcuts import render, get_object_or_404, redirect
from .models import Worker
from .forms import WorkerForm

# List all workers (READ)
def worker_list(request):
    workers = Worker.objects.all()
    return render(request, 'workers/worker_list.html', {'workers':workers})

# Create a new worker (CREATE)
def worker_new(request):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker = form.save()
            return redirect('worker_detail', pk=worker.pk)
    else:
        form = WorkerForm()
    return render(request, 'workers/worker_edit.html', {'form': form})

# Edit an existing worker (UPDATE)
def worker_edit(request, pk):
    worker = get_object_or_404(worker, pk=pk)
    if request.method =="POST":
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            worker = form.save()
            return redirect('worker_detail', pk=worker.pk)
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'workers/worker_edit.html', {'form': form})

# Delete a worker (DELETE)
def worker_delete(request,pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method =='POST':
        worker.delete()
        return redirect('worker_list')
    return render(request, 'workers/worker_confirm_delete.html', {'worker': worker})
    
        

