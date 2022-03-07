from pydoc import describe
from pyexpat import model
from django.db import models


MEALS =(
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


class Bird(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    age = models.IntegerField()

    def __str__(self):
        return self.name

        
class Feeding(models.Model):
    date = models.DateField('Feeding Date')
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
