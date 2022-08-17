from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import *


class CreateUserForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'Username','class':' form-control ', 'type':'text', }))
    email = forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'Email','class':' form-control ', 'type':'text', }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'Password','class':' form-control ', 'type':'password', }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'Confirm Your Password','class':' form-control ', 'type':'password', }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class FoodForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    serving_size = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    protein = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    carbs = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    fat = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    sugar = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    stauratedFat = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    kilojoules = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))


    class Meta:
        model = Food
        fields = '__all__'


class ExerciseForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    muscleGroup = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    xpGained = forms.CharField(widget=forms.TextInput(attrs={'class':' form-control ', 'type':'text', }))
    class Meta:
        model = Exercise
        fields = '__all__'