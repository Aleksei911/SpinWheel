from django.urls import path
from rest_framework import routers
from .views import RoundCurrentValuesView, LogView, index, statistics

urlpatterns = [
    path('', index, name='index'),
    path('stat/', statistics, name='stat'),
]

router = routers.DefaultRouter()
router.register('round', RoundCurrentValuesView)
router.register('log', LogView)

urlpatterns += router.urls
