from django.shortcuts import render, redirect
from .models import Player, Team
from django.contrib import messages

# Create your views here.


def homePage(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    messages.success(request, 'Got Teams Successfully')
    return render(request, "manageTeam.html", {"teams": teams, "players": players})

def playerPage(request):
    teams = Team.objects.all()
    players = Player.objects.all()
    messages.success(request, 'Got Players Successfully')
    return render(request, "managePlayer.html", {"players": players, "teams": teams})


def registerPlayer(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    player = Player.objects.create(first_name=first_name, last_name=last_name)
    messages.success(request, 'Player has been registered')
    return redirect('/players')


def getPlayer(request, id):
    player = Player.objects.get(id=id)
    return render(request, "getPlayer.html", {"player": player})


def editPlayer(request):
    id = request.POST['id']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']

    player = Player.objects.get(id=id)
    player.first_name = first_name
    player.last_name = last_name
    player.save()

    messages.success(request, 'Player has been updated')

    return redirect('/players')


def deletePlayer(request, id):
    player = Player.objects.get(id=id)
    player.delete()

    messages.success(request, 'Player has been deleted')

    return redirect('/players')

def registerTeam(request):
    city = request.POST['city']
    mascot = request.POST['mascot']
    players = request.POST.getlist('players')

    team = Team.objects.create(city=city, mascot=mascot)
    team.players.set(players)
    messages.success(request, 'New Team has been registered')
    return redirect('/')


def getTeam(request, id):
    team = Team.objects.get(id=id)
    teamPlayers = team.players.all()
    playerIds = [p.id for p in teamPlayers]
    players = Player.objects.all()
    return render(request, "getTeam.html", {"team": team, "players": players, "playerIds": playerIds})


def updateTeam(request):
    id = request.POST['id']
    city = request.POST['city']
    mascot = request.POST['mascot']
    players = request.POST.getlist('players')

    team = Team.objects.get(id=id)
    team.city = city
    team.mascot = mascot
    team.players.set(players)
    team.save()

    messages.success(request, 'Team has been updated')

    return redirect('/')


def deleteTeam(request, id):
    team = Team.objects.get(id=id)
    team.delete()

    messages.success(request, 'Team has been deleted')

    return redirect('/')
