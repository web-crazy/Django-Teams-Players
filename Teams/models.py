from django.db import models
from django.contrib import admin

# Create your models here.


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.first_name, self.last_name)

class Team(models.Model):
    city = models.CharField(max_length=50)
    mascot = models.CharField(max_length=50)
    players = models.ManyToManyField(Player, through='TeamContainsPlayer', related_name='player', blank=True)

    def __str__(self):
        return self.city + " - " + self.mascot

class TeamContainsPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

class TeamInline(admin.TabularInline):
    model = Team.players.through

class TeamAdmin(admin.ModelAdmin):
    inlines = (TeamInline,)
    exclude = ('players',)
