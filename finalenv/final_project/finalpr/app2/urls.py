from . import views
from django.urls import path

urlpatterns=[
    path('', views.demo, name='demo'),
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('reg_form',views.reg_form,name='reg_form'),
    path('logout',views.logout,name='logout')
]