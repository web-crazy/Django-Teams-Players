from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('players', views.playerPage),
    path('registerPlayer/', views.registerPlayer),
    path('getPlayer/<id>', views.getPlayer),
    path('updatePlayer/', views.editPlayer),
    path('deletePlayer/<id>', views.deletePlayer),
    path('registerTeam/', views.registerTeam),
    path('getTeam/<id>', views.getTeam),
    path('updateTeam/', views.updateTeam),
    path('deleteTeam/<id>', views.deleteTeam),
]
