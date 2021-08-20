from cbvApp.models import Employee
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView

# Create your views here.
class EmployeeList(ListView):
     model = Employee
     template_name = 'empList.html'

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'empDetail.html'
    context_object_name = 'employee_detail'
