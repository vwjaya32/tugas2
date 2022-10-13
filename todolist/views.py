from django.shortcuts import render
from todolist.models import Task

from django.http import HttpResponse, JsonResponse
from django.core import serializers

# REGISTER
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# LOGIN
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# LOGOUT
from django.contrib.auth import logout

# FORMS
from .forms import NewTaskForm


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    # data = Task.objects.filter(user=request.user)
    # context = {
    #     'data_list' : data    
    # }
    return render (request, "todolist.html")

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def new_task(request):
    if request.method == 'POST' :
        form = NewTaskForm(request.POST)
        
        if form.is_valid():
            data      = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('todolist:show_todolist')
        
    else:
        form = NewTaskForm()
    
    return render(request, 'newtask.html', {'form': form})

def remove_task(request, id):
    target = Task.objects.get(pk=id)
    target.delete()
    return redirect('todolist:show_todolist')

def status(request, id):
    target = Task.objects.get(pk=id)
    
    target.is_finished = False if target.is_finished else True
    target.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        
        if form.is_valid():
            data      = form.save(commit=False)
            data.user = request.user
            data.save()
            form.save_m2m()
        return HttpResponse(serializers.serialize('json', [data, ]), content_type='application/json')
        
