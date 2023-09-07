from django.db.models import Sum, Count, Case, When, Avg
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import RoundCurrentValues, Log
from .serializers import RoundCurrentValuesSerializer, LogSerializer


class RoundCurrentValuesView(ModelViewSet):
    queryset = RoundCurrentValues.objects.all()
    serializer_class = RoundCurrentValuesSerializer

    def perform_create(self, serializer):
        serializer.save(player=self.request.user)


class LogView(ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    def perform_create(self, serializer):
        serializer.save(name=self.request.user)


def index(request):
    return render(request, 'main/index.html')


def statistics(request):
    players = Log.objects.values('round_number', 'name').distinct()
    context = {
        'players': players,
    }
    return render(request, 'main/stat.html', context)

