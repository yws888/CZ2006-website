from django.urls import path
from . import views
from .views import HDBResaleFlatView



urlpatterns = [
    path('', views.home, name='househunt-home'),
    path('about/', views.about, name='househunt-about'),
    path('calculate/',views.calculate, name='househunt-calculate'),
    path('calculate/result/',views.result, name='househunt-result'),
    path('visualise/',views.visualise, name='househunt-visualise'),
    path('search/',views.search, name='househunt-search'),
    path('search/result/',views.search_result, name='househunt-search-result'),
    # path('search/result/',HDBResaleFlatView.as_view(), name='househunt-search-result'),

]