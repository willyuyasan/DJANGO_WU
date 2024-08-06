from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate #create the user cookie, end the session


from .serializer import TaskSerializer
from .models import Task
from .forms import TaskForm

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

def greeting(request):
    return HttpResponse('Hello developer')

def home(request):
    return render(request, 'home.html')

def signup(request):

    usercform = UserCreationForm

    if request.method == 'GET':
        print(request.method)
        print('Recieving form')
    else:
        #print(request.POST)
        #print('Sending form')
        if request.POST['password1'] == request.POST['password2']:
            try:
                #register the user
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )
                user.save() #saves the user into the DB
                login(request,user)
                return redirect('tasks')

            except:
                return render(request, 'signup.html', {
                    'usercform': usercform,
                    'error':'user already exists!'
                })
   
        else:
            return render(request, 'signup.html', {
                    'usercform': usercform,
                    'error':'passwords does not match!'
                })

    #return HttpResponse('<h1> Hello everybody </h1>')
    return render(request, 'signup.html', {
        'usercform': usercform
    })

def tasks(request):
    #tasks_ls = Task.objects.all() #List all the task
    tasks_ls = Task.objects.filter(user=request.user) #List the task from actual user
    return render(request, 'tasks.html', {
        'task_ls':tasks_ls
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'taskform': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except:
            return render(request, 'create_task.html', {
            'taskform': TaskForm,
            'error': 'Please provide valid data'
            })

def task_details(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    print(task)
    return render(request, 'task_details.html', {
        'task':task
    })

def close_session(request):
    logout(request)
    return redirect('home')

def signin(request):
    useraform = AuthenticationForm
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'useraform': useraform
        })
    else:
        #print(request.POST)
        user = authenticate(request,
            username = request.POST['username'],
            password = request.POST['password'],
        )
        if user==None:
            return render(request, 'signin.html', {
                'useraform': useraform,
                'error': 'Username or password incorrect'
            })
        else:
            login(request,user)
            return redirect('tasks')

    return render(request, 'signin.html', {
                'useraform': useraform,
            })

