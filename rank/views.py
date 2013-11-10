from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import render_to_response, HttpResponseRedirect
from Users.models import JadeBusemUser
from rank.models import Rank, RankLive
from datetime import datetime
import urllib
import string
import re

def rank(request):
    if 'email' in request.session:
            return render_to_response('rank.html', {'user': request.session['name'],
                                                    'login': True})
    else:
        return render_to_response('rank.html',
                                  {'login': False})

def ranking_live_update(request):
    users = JadeBusemUser.objects.all()
    for user in users:
        if user.is_active and user.link != "":
            sock = urllib.urlopen(user.link)
            htmlSource = sock.read()
            sock.close()
            findme   = 'Battles Participated'
            findmee   = 'Vehicle'
            start = string.find(htmlSource, findme)
            end = string.find(htmlSource, findmee)
            htmlSource = htmlSource[start:end]
            htmlSource = re.sub("<[^<>]*>", "", htmlSource)
            htmlSource = string.replace(htmlSource, ",", "")
            htmlSource = string.replace(htmlSource, " ", "")
            htmlSource = re.sub("[^0-9]+", " ", htmlSource)
            htmlSource = htmlSource.split(" ")
            try:
                rank = RankLive.objects.get(name=user.name)
                try:
                    rank2 = Rank.objects.get(name=user.name).order_by('-date')
                except MultipleObjectsReturned:
                    rank2 = Rank.objects.filter(name=user.name).order_by('-date')[0]
                liczba = (int(htmlSource[1]) - int(rank2.participated))
                if liczba == 0:
                    liczba = 1
                rank.participated = str(int(htmlSource[1]) - int(rank2.participated))
                rank.win = str(int(htmlSource[2]) - int(rank2.win))
                rank.defeat = str((int(htmlSource[13]) - int(rank2.dmg)) / liczba)
                rank.survive = str(int(htmlSource[5]) - int(rank2.survive))
                rank.destroyed = str(int(htmlSource[10]) - int(rank2.destroyed))
                rank.spoted = str(int(htmlSource[11]) - int(rank2.spoted))
                rank.shootPercent = str(int(htmlSource[12]) - int(rank2.shootPercent))
                rank.dmg = str(int(htmlSource[13]) - int(rank2.dmg))
                rank.ocupated = str(int(htmlSource[15]) - int(rank2.ocupated))
                rank.defense = str(int(htmlSource[16]) - int(rank2.defense))
                rank.exp = str(int(htmlSource[7]) - int(rank2.exp))
                rank.severalExp = str(int(htmlSource[8]) - int(rank2.severalExp))
                rank.maxExp = str(int(htmlSource[9]) - int(rank2.maxExp))
                rank.date = datetime.now()
                rank.save()
            except RankLive.DoesNotExist:
                rank = RankLive(name=user.name, participated=0, win=0, defeat=0, survive=0, destroyed=0, spoted=0, shootPercent=0, dmg=0, ocupated=0, defense=0, exp=0, severalExp=0, maxExp=0)
                rank.save()
                try:
                    rank2 = Rank.objects.get(name=user.name)
                except  Rank.DoesNotExist:
                    rank2 = Rank(name=user.name, participated=htmlSource[1], win=htmlSource[2], defeat=htmlSource[3], survive=htmlSource[5], destroyed=htmlSource[10], spoted=htmlSource[11], shootPercent=htmlSource[12], dmg=htmlSource[13], ocupated=htmlSource[15], defense=htmlSource[16], exp=htmlSource[7], severalExp=htmlSource[8], maxExp=htmlSource[9])
                    rank2.save()
    return HttpResponseRedirect('/rank/')

def ranking_update(request):
    users = JadeBusemUser.objects.all()
    for user in users:
        if user.is_active and user.link != "":
            sock = urllib.urlopen(user.link)
            htmlSource = sock.read()
            sock.close()
            findme   = 'Battles Participated'
            findmee   = 'Vehicle'
            start = string.find(htmlSource, findme)
            end = string.find(htmlSource, findmee)
            htmlSource = htmlSource[start:end]
            htmlSource = re.sub("<[^<>]*>", "", htmlSource)
            htmlSource = string.replace(htmlSource, ",", "")
            htmlSource = string.replace(htmlSource, " ", "")
            htmlSource = re.sub("[^0-9]+", " ", htmlSource)
            htmlSource = htmlSource.split(" ")
            rank = Rank(name=user.name, participated=htmlSource[1], win=htmlSource[2], defeat=htmlSource[3], survive=htmlSource[5], destroyed=htmlSource[10], spoted=htmlSource[11], shootPercent=htmlSource[12], dmg=htmlSource[13], ocupated=htmlSource[15], defense=htmlSource[16], exp=htmlSource[7], severalExp=htmlSource[8], maxExp=htmlSource[9])
            rank.save()
    return render_to_response('rank.html', {'login': False})

def show_ranking(request):
    if 'email' in request.session:
        rank = RankLive.objects.all()
        return render_to_response('rank.html', {'login': True,
                                            'rank': rank,
                                            'user': request.session})
    else:
        rank = RankLive.objects.all()
        return render_to_response('rank.html', {'login': False,
                                            'rank': rank,
                                            'user': request.session})