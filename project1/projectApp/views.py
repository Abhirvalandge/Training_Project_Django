from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from projectApp.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from .models import Product


# Create your views here.
@login_required
def indexView(request):
    return render(request, 'templates/registration/login.html')

@login_required
def showProduct(request):
    products = Product.objects.all()
    return render(request,"products.html",{"products":products})

def signupView(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,"signup.html", {'form':form})

def signinView(request):
    products = Product.objects.all()
    return render(request,'products.html',{"products":products})

def dashboardView(request):
    return render(request,"dashboard.html")

def logout_view(request):
     return render(request,"logout.html")    
    

