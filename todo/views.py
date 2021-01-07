from django.shortcuts import render,HttpResponse,redirect
from .forms import TodoForm
from django.contrib import messages
from todo.models import Todos

# Create your views here.
def index(request): 
    todo = Todos.objects.all().order_by('-created_date')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            messages.error(request,'please fill proper detail')
            return redirect('index')
    else:
        form = TodoForm() 
    return render(request,'todo/index.html',{'form':form,'todo':todo})


def deletetodo(request,id):
    deltodo = Todos.objects.get(id=id)
    deltodo.delete()
    return redirect('index')