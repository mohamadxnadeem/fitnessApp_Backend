from django.db import models
from django.contrib.auth.models import User
import math 


# Create your models here.

'''


class Exercises(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    muscleGroup = name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

'''

# First we going to work on the Diet an water intake

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    age = models.CharField(max_length=200, null=True)
    weight = models.IntegerField(default=0, null=True, blank=True)

    maxbenchpress = models.IntegerField(default=0, null=True, blank=True)
    maxsquat = models.IntegerField(default=0, null=True, blank=True)
    maxdeadlift = models.IntegerField(default=0, null=True,  blank=True)


    def __str__(self):
        return self.name

    @property
    def Your_BMI(self):
        bmi = self.weight / (self.height)**2
        return total


    """
    @property
        def Your_strength_level(self):
            bmi = self.weight / (self.height)**2
            return total
    """



class Food(models.Model):

    name = models.CharField(max_length=200, null=True, blank=True)
    serving_size = models.CharField(max_length=200, null=True, blank=True)
    protein = models.FloatField( null=True, blank=True)
    carbs = models.FloatField( null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    sugar = models.FloatField( null=True, blank=True)
    stauratedFat = models.FloatField( null=True, blank=True)
    kilojoules = models.FloatField( null=True, blank=True)


    def __str__(self):
        return self.name



class Water(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ml = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name



# Then we going to work on the workout sie of things

# Exercises source myEnv/bin/activate 



class Exercise(models.Model):
    name = models.CharField(max_length=200,  null=True, blank=True)
    description = models.CharField(max_length=200,  null=True, blank=True)
    muscleGroup = models.CharField(max_length=200,  null=True, blank=True)
    xpGained = models.FloatField( null=True, blank=True)
    
    def __str__(self):
        return self.name


        

# Workout routine based on goals
# The API should collect and display data for the user
# The user should get XP when ever a exercise is completed
# The user should be able to create custom workout
# There will be a challenge for each user to gain extra xp if completed



'''

class WorkoutRoutine(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    muscleGroup = name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name




class strengthLevel(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    muscleGroup = name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



class xp(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    muscleGroup = name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    '''

