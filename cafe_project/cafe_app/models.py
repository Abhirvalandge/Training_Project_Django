from django.db import models

# Create your models here.
class CoffeeModel(models.Model):
    coffee_name = models.CharField(max_length=50)
    hot = models.CharField(max_length=50)
    iced = models.CharField(max_length=50)
    blended = models.CharField(max_length=50)

    def __str__(self):
        return self.coffee_name

class TeaModel(models.Model):
    tea_name = models.CharField(max_length=50)
    hot = models.CharField(max_length=50)
    iced = models.CharField(max_length=50)
    addon = models.CharField(max_length=50)

    def __str__(self):
        return self.tea_name

class SnacksModel(models.Model):
    snacks_name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.snacks_name
