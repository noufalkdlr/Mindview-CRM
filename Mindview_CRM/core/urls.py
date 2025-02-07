from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('',views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('home/',views.home_view, name='home'),
    
]
