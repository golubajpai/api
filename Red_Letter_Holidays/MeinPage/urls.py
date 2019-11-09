from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    
	path('',Data.as_view(),name='index'),
	path('register/',UserCreateAPIView.as_view(),name='user'),
	path('login/',Login.as_view(),name='login'),
	path('logout/',Logout.as_view(),name='logout'),

]
