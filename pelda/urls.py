from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name="login"),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('kapcsolat/', views.kapcsolat, name="kapcsolat"),
    path('rolunk/', views.rolunk, name="rolunk"),
    path('feladat/', views.feladat, name="feladat"),
    path('terulet/', views.terulet, name="terulet"),
]