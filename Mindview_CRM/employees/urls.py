from django.urls import path

from . import views

app_name = 'employees'

urlpatterns = [
    path('',views.employees, name='employees'),
    path('<slug:slug>/',views.employee_detail, name='emp_detail'),
]
