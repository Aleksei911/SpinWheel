from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from .views import RoundCurrentValuesView, LogView, index, statistics

urlpatterns = [
    path('', index, name='index'),
    path('stat/', csrf_exempt(statistics), name='stat'),
]

router = routers.DefaultRouter()
router.register('round', RoundCurrentValuesView)
router.register('log', LogView)

urlpatterns += router.urls
