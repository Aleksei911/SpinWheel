from django.contrib.auth.models import User
from django.db import models


class RoundCurrentValues(models.Model):
    player = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    round_number = models.PositiveIntegerField()
    value = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.player} - round {self.round_number} - value {self.value}'


class Log(models.Model):
    name = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, related_name='player')
    round_number = models.PositiveIntegerField()
    value = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.name} - round {self.round_number} - value {self.value}'


