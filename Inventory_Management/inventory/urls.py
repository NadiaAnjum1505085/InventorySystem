from django.urls import path
#from . import views
from rest_framework.authtoken import views

app_name='Inventory'
urlpatterns = [
    # path('',views.index,name='index'),
    # path('register/',views.register,name='register'),
    # path('login/',views.login,name='login'),
    # path('token/',views.TokenCreate,name='token'),
    path('api-token-auth/', views.obtain_auth_token),
]
