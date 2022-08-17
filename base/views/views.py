from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from ..forms import CreateUserForm, FoodForm, ExerciseForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from ..models import *

#pagination imports:

from django.core.paginator import Paginator


#=============================================================================


#Authentication views:


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)
                return redirect('login')

        context = {'form':form}
        return render (request, 'base/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method =='POST':
            
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else: 
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render (request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
    

#=============================================================================

# Home Page


@login_required(login_url='login')
def home(request):
 
    context = {}
    return render (request, 'base/index.html', context)


#=============================================================================

# Users page

@login_required(login_url='login')
def users(request):
    user_count = Profile.objects.count()
    users = Profile.objects.all()

    p = Paginator(Profile.objects.all(), 10)
    page = request.GET.get('page')
    venues = p.get_page(page)

    context = {
        'users':users,
        'user_count':user_count,
        'venues':venues,
        }
    return render (request, 'base/users.html', context)



#=============================================================================

# Exercises pages:

@login_required(login_url='login')
def exercises(request):

    # all objects:
    exercise = Exercise.objects.all()

    exercise_count = Exercise.objects.count()
    form = ExerciseForm()

    #pagination setup

    p = Paginator(Exercise.objects.all(), 10)
    page = request.GET.get('page')
    venues = p.get_page(page)

    # boolean statement:

    if request.method == "POST":
        #print('printing post:', request.post)
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/exercises')


    # context dictionary:

    context = {
        'exercise':exercise,
        'form':form,
        'venues':venues,
        'exercise_count':exercise_count,
    
    }

    #returns template and renders objects to the page using the context dictionary
    return render (request, 'base/exercises.html', context )


@login_required(login_url='login')
def updateExercise(request,pk):
   
    exercise = Exercise.objects.get(id=pk)
    form =  ExerciseForm(instance=exercise)

    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('/exercises')

    context = { 'form':form }
    return render ( request, 'base/update_exercise.html', context )

@login_required(login_url='login')
def deleteExercise(request, pk):

    exercise = Exercise.objects.get(id=pk)

    if request.method == 'POST':
        exercise.delete()
        return redirect('/exercises')


    context = {'exercise':exercise,}
    return render(request, 'base/delete_exercise.html', context)


#=============================================================================

#food pages:


@login_required(login_url='login')
def food(request):

    food = Food.objects.all()
    form = FoodForm()
    food_count = Food.objects.count()


    p = Paginator(Food.objects.all(), 10)
    page = request.GET.get('page')
    venues = p.get_page(page)



    if request.method == "POST":
        #print('printing post:', request.post)
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/food')
    context = {
        'food':food,
        'form':form,
        'venues':venues,
        'food_count':food_count,
    
     }
    return render (request, 'base/food.html', context)



@login_required(login_url='login')
def updateFood(request,pk):
   
    food = Food.objects.get(id=pk)
    form =  FoodForm(instance=food)

    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('/food')

    context = { 'form':form ,
    
    }
    return render ( request, 'base/update_food.html', context )


@login_required(login_url='login')
def deleteFood(request, pk):

    food = Food.objects.get(id=pk)
    
    if request.method == 'POST':
        food.delete()
        return redirect('/food')

    context = {
        'food':food,
        
        }
    return render(request, 'base/delete_food.html', context)


#=============================================================================



