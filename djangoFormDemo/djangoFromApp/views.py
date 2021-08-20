from djangoFromApp.forms import EmployeeForm
from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def indexView(request):
    return render(request,"index.html")

def createView(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                # return HttpResponse("Successfully Submitted")
                return redirect('/retrive')
            except:
                print("not saved")
                
    else:
        form = EmployeeForm()
        return render(request, 'create.html', {'form': form})\


def retrieveView(request):
    employee = Employee.objects.all()
    return render(request, 'retrieve.html', {'employee': employee})


