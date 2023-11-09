from django.contrib import admin
from django.urls import path,include
from attendance import views

urlpatterns = [
    path('',views.home,name='home.html'),
    path('index/',views.index,name='index.html'),
    path('login/',views.login,name='login.html'),
    path('review/',views.review,name='review.html'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register')
]