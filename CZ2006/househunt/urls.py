from django.urls import path
from . import views
from .views import HDBResaleFlatView



urlpatterns = [
    path('', views.home, name='househunt-home'),
    path('about/', views.about, name='househunt-about'),
    path('calculate/',views.calculate, name='househunt-calculate'),
    path('calculate/result/',views.result, name='househunt-result'),
    path('visualise/',views.visualise, name='househunt-visualise'),
    path('visualise/town/',views.visualise_town, name='househunt-visualise-town'),
    path('visualise/flat-type/',views.visualise_flat_type, name='househunt-visualise-flat-type'),
    path('visualise/year/',views.visualise_year, name='househunt-visualise-year'),
    path('search/',views.search, name='househunt-search'),
    path('search/<int:price>',views.searchPrice, name='househunt-search'),
    path('search/result/',views.search_result, name='househunt-search-result'),

    path('estimate/',views.estimate, name='househunt-estimate'),
    path('estimate/result/',views.estimate_result, name='househunt-estimate-result'),
    #path('search/result/',HDBResaleFlatView.as_view(), name='househunt-search-result'),
    path('map/<int:id>/',views.map, name='househunt-map'),

]