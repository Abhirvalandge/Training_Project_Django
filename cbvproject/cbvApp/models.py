from django.db import models

# Create your models here.
class Employee(models.Model):
    empNo = models.CharField(max_length=100)
    empName = models.CharField(max_length=100)
    empMobile = models.CharField(max_length=100)
    empEmail = models.EmailField()

    def __str__(self):
        return self.empName
