from django.contrib import admin
from .models import Player, Team, TeamAdmin

# Register your models here.

admin.site.register(Player)
admin.site.register(Team, TeamAdmin)
