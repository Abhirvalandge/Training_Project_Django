from django.shortcuts import render
from .models import *


# Create your views here.
def indexView(request):
    return render(request,'index.html')

def coffeeView(request):
    data = CoffeeModel.objects.all()
    return render(request,'coffee.html', {'data':data})


def teaView(request):
    data = TeaModel.objects.all()
    return render(request,'tea.html', {'data':data})


def snacksView(request):
    data = SnacksModel.objects.all()
    return render(request,'snacks.html', {'data':data})


