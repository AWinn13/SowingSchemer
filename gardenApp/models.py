from django.db import models



# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SeedJournal(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)


class Garden(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    unitOfMeasure = models.CharField(max_length=4)
    gardenNumber = models.IntegerField()
    nickname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vegetable(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    garden  = models.ForeignKey(Garden, on_delete= models.CASCADE)
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
    id = models.IntegerField(primary_key=True, editable=False)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField()
    completed = models.TextField(blank=True)
    todo = models.TextField(blank=True)
    soilTemp = models.IntegerField(blank=True)
    airTemp = models.IntegerField(blank=True)
    weather = models.CharField(max_length=150, blank=True)
    planted = models.TextField(blank=True)
    entry = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)