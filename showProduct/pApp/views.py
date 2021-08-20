from pApp.models import Product
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from pApp.forms import SignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def showProduct(request):
    products = Product.objects.all()
    return render(request,"product.html",{"products":products})
def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,"signup.html",{'form':form})

def logout_view(request):
     return render(request,"logout.html")    