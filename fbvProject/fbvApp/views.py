from django.shortcuts import render,redirect
from fbvApp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Sum,Max,Min


# Create your views here.
def retrieveView(request):
    data = Employee.objects.all()

    #Aggregate Functions
    avg1 = Employee.objects.all().aggregate(Avg('empSal'))
    max = Employee.objects.all().aggregate(Max('empSal'))
    min = Employee.objects.all().aggregate(Min('empSal'))
    sum = Employee.objects.all().aggregate(Sum('empSal'))

    return render(request,'showIndex.html',{'data':data})

def deleteView(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')