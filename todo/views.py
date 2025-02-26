from django.shortcuts import render, redirect 
from .models import Task
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# these views are very good. ( this line is only for testing git pourposes``)

########################################
# default login page
########################################
def index(request):

    return render (request, 'todo/index.html')


########################################
# sign up page
########################################
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password, email=email) 
            '''
                notice then create_user() method above. this is one of the ways of creating a user in django.
                remember that the default fields of user in the database are  username, password, email, first_name, last_name, and that's why we specify them when signing him in.
                later, make sure to use the form from this model instead of creating your own.
            '''
            user.save()
            return redirect('todo:log_in')
    else:
        form = SignupForm()
    #     return redirect('todo:log_in')
    return render(request, 'todo/signup.html', {'form': form})

#######################################
# authenticate a user using both authenticate and login methods
#######################################
def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        # check if the form is valid.
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #check if the user is authenticated
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo:home')
            else:
                form = LoginForm()
                error_message = 'wrong username or password'
                context = {
                    'form' : form,
                    'error_message' : error_message
                }
                return render(request, 'todo/login.html', context)

    else:
        form = LoginForm()
        return render(request, 'todo/login.html', {"form":form})


#######################################
# home page to display all tasks
#######################################
'''
the login_required decorator redirects the user to settings.LOGIN_URL. this means that you have to specify the 
url to the login page in the settings. if you don't, then you will have to pass the 'login_url' argument to the decorator

if the user is logged in, then the view executes normally. (the view is free to assume that the user is loggen in, haha)

it takes an optional 'redirect_field_name' to override the word 'next' which tells where the login redirect should enter.
'''
@login_required(redirect_field_name=None) # decorator requiring login
def home(request):
    # check iif not request.user.is_authenticated:
    #     return redirect('todo:log_in')f the user is authenticated (the raw way)
    # if not request.user.is_authenticated:
    #     return redirect('todo:log_in')
    
    completed_tasks = Task.objects.filter(completed=True, user=request.user).order_by('-updated_at')
    incomplete_tasks = Task.objects.filter(completed=False, user=request.user).order_by('-updated_at')
    return render(request, 'todo/home.html', context={'completed_tasks': completed_tasks, 'incomplete_tasks': incomplete_tasks})
    

#######################################
# add a new task
#######################################
def addtask(request):
    if request.method == 'POST':
        description = request.POST['description']
        Task.objects.create(description=description, user=request.user)
        return redirect('todo:home')
    else:
        return render(request, 'todo/addtask.html')
    

#######################################
# task
#######################################
def task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'todo/task.html', context={'task': task})


#######################################
# update a task
#######################################
def updatetask(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        description = request.POST['description']
        task.description = description
        task.save()
        return redirect('todo:home')
    else:
        return render(request, 'todo/updatetask.html', context={'task': task})


#######################################
# mark a task as complete or incomplete
#######################################
def complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.completed:
        task.completed = False
    else:
        task.completed = True
    task.save()
    return redirect('todo:home')


#######################################
# delete a task
#######################################
def deletetask(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('todo:home')


########################################
#       LOG OUT
########################################
def log_out(request):
    logout(request)
    return redirect('todo:log_in')

