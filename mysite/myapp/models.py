from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class food(models.Model):

    def __str__(self):
        return(self.name)
    name=models.CharField(max_length=200)
    carbs=models.FloatField()
    protein=models.IntegerField()
    fats=models.FloatField()
    calories=models.IntegerField()

class Consume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    food_consumed=models.ForeignKey(food,on_delete=models.CASCADE)    