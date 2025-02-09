from django.urls import path

from . import views

app_name = 'employees'

urlpatterns = [
    path('',views.employees, name='employees'),
    path('add-employee/', views.add_employee, name='emp_add'),
    path('<slug:slug>/',views.employee_detail, name='emp_detail'),
    path('<slug:slug>/delete/', views.employee_delete, name='emp_delete'),
    

]
