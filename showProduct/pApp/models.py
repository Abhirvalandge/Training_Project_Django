from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category 
class Product(models.Model):
    Category_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    decription = models.TextField(blank=True)
    image = models.ImageField(upload_to="product\images")

    
    def __str__(self):
        return self.product_name    