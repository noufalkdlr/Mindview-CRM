from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages

from .models import EmployeesDetails
from .forms import EmployeesDetailsForm

# Create your views here.

def employees(request):
    
    emp_list = EmployeesDetails.objects.all()

    return render(request,'employees/employees_list.html',{'emp_list': emp_list})


def employee_detail(request, slug):
    employee = get_object_or_404(EmployeesDetails, slug=slug)
    return render(request,'employees/employee_detail.html',{'employee':employee})


def employee_delete(request, slug):
    employee = get_object_or_404(EmployeesDetails, slug= slug)
    employee.delete()
    messages.success(request,"Employee deleted successfully!")
    return redirect('employees:employees')


def add_employee(request):

    if request.method == 'POST':
        form = EmployeesDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees:employees')
        
    else:
        form = EmployeesDetailsForm()

    return render(request, 'employees/add_employee.html',{'form':form})

