from django.db import models
from django.forms import ModelForm
from django import forms


# Create your models here.


class PostForm(models.Manager):
    # this function will be used for the validation
    def clean(self, postData):
        # data from the form is fetched using super function
        errors = {}

        # conditions to be met for the username length
        if len(postData['first_name']) < 1:
            errors["first_name"] = "Minimum 1 characters required"
        if len(postData['last_name']) < 1:
            errors["text"] = "Last Name must be at least 1 character"
        if len(postData['email']) < 4:
            errors["email"] = "Minimum 4 characters required"
        if len(postData['password']) < 7:
            errors["password"] = "Password must be at least 7 characters"

        # return any errors if found
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostForm()


class SeedJournal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Garden(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    unitOfMeasure = models.CharField(max_length=4)
    gardenNumber = models.IntegerField()
    nickname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vegetable(models.Model):
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    variety = models.CharField(max_length=100)
    numOfPlants = models.IntegerField()
    amountOfSun = models.CharField(max_length=15)
    length = models.IntegerField()
    width = models.IntegerField()
    datePlanted = models.DateField(null=True)
    seedling = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GardenJournal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    completed = models.TextField(blank=True)
    todo = models.TextField(blank=True)
    soilTemp = models.IntegerField(blank=True)
    airTemp = models.IntegerField(blank=True)
    weather = models.CharField(max_length=150, blank=True)
    planted = models.TextField(blank=True)
    observation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
