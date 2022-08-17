from django.urls import path
from base.views import views


urlpatterns = [

    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    

    path('', views.home, name='home'),
    path('users/', views.users, name='users'),


    path('exercises/', views.exercises, name='exercises'),
    path('update_exercise/<str:pk>/', views.updateExercise, name='update_exercise'),
    path('delete_exercise/<str:pk>/', views.deleteExercise, name='delete_exercise'),

    path('food/', views.food, name='food'),
    path('update_food/<str:pk>/', views.updateFood, name='update_food'),
    path('delete_food/<str:pk>/', views.deleteFood, name='delete_food'),


  
    

]