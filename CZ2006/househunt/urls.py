from django.urls import path
from . import views
from .views import (
     AboutView,
    Visualise, VisualiseTown, VisualiseFlatType, VisualiseYear
)

urlpatterns = [
    path('', views.HomeView.as_view(), name='househunt-home'),
    path('about/', AboutView.as_view(), name='househunt-about'),
    path('calculate/',views.calculate, name='househunt-calculate'),
    path('calculate/result/',views.result, name='househunt-result'),
    path('visualise/',Visualise.as_view(), name='househunt-visualise'),
    path('visualise/town/',VisualiseTown.as_view(), name='househunt-visualise-town'),
    path('visualise/flat-type/',VisualiseFlatType.as_view(), name='househunt-visualise-flat-type'),
    path('visualise/year/',VisualiseYear.as_view(), name='househunt-visualise-year'),
    path('search/',views.search, name='househunt-search'),
    path('search/<int:price>',views.searchPrice, name='househunt-search'),
    path('search/result/',views.search_result, name='househunt-search-result'),
    path('estimate/',views.estimate, name='househunt-estimate'),
    path('estimate/result/',views.estimate_result, name='househunt-estimate-result'),
    path('map/<int:id>/',views.map, name='househunt-map'),

]
