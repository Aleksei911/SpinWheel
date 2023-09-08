from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Count, Case, When, Avg, Value, F
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


@csrf_exempt
def statistics(request):
    players = Log.objects.values('round_number').distinct().annotate(
        users=Count('name', distinct=True)
    ).values('round_number', 'users')

    activity = Log.objects.values('name').distinct().annotate(
        rounds=Count('round_number', distinct=True),
        avg_spins=Count('value') / Count('round_number', distinct=True)
    ).values('name', 'rounds', 'avg_spins')
    context = {
        'players': players,
        'activity': activity,
    }
    return render(request, 'main/stat.html', context)

