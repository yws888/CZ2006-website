from django.urls import path
from . import views
from .views import (
     AboutView,
    Visualise, VisualiseTown, VisualiseFlatType, VisualiseYear
)

urlpatterns = [
    path('', views.HomeView.as_view(), name='househunt-home'),
    path('about/', AboutView.as_view(), name='househunt-about'),
    path('calculate/',views.CalculateView.as_view(), name='househunt-calculate'),
    path('calculate/result/',views.CalculateView.as_view(), name='househunt-result'),
    path('visualise/',Visualise.as_view(), name='househunt-visualise'),
    path('visualise/town/',VisualiseTown.as_view(), name='househunt-visualise-town'),
    path('visualise/flat-type/',VisualiseFlatType.as_view(), name='househunt-visualise-flat-type'),
    path('visualise/year/',VisualiseYear.as_view(), name='househunt-visualise-year'),
    path('search/',views.SearchView.as_view(), name='househunt-search'),
    path('search/<int:price>',views.SearchWithPriceView.as_view(), name='househunt-search-w-price'),
    path('search/result/',views.SearchResultView.as_view(), name='househunt-search-result'),
    path('estimate/',views.EstimateView.as_view(), name='househunt-estimate'),
    path('estimate/result/',views.EstimateView.as_view(), name='househunt-estimate-result'),
    path('map/<int:id>/',views.MapView.as_view(), name='househunt-map'),

]
