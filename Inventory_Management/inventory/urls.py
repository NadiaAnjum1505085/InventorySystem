from django.urls import path
from . import views

app_name='Inventory'
urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
]
