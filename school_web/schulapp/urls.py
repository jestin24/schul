from django.urls import path
from . import views

app_name ='schulapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('log/',views.log, name='log'),
    path('register/',views.register, name='register'),
    path('reg/',views.reg, name='reg'),
    path('wel/',views.wel, name='wel'),
    path('sub/', views.sub, name='sub'),

 ]