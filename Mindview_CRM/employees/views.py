from django.shortcuts import render,get_object_or_404

from .models import EmployeesDetails

# Create your views here.

def employees(request):
    
    emp_list = EmployeesDetails.objects.all()

    return render(request,'employees/employees_list.html',{'emp_list': emp_list})


def employee_detail(request, slug):
    employee = get_object_or_404(EmployeesDetails, slug=slug)
    return render(request,'employees/employee_detail.html',{'employee':employee})