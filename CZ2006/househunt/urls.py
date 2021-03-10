from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='househunt-home'),
    path('about/', views.about, name='househunt-about'),
    path('calculate/',views.calculate, name='househunt-calculate'),
    path('calculate/result/',views.result, name='househunt-result'),
    path('visualise/',views.visualise, name='househunt-visualise'),

]