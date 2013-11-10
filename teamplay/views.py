# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from teamplay.models import Team
from datetime import datetime
import string

def teamplay(request):
    team = Team.objects.all().order_by('-date')
    if 'email' and 'name' in request.session:
            date=datetime.now()
            return render_to_response('teamplay/teamplay.html', {'user': request.session,
                                                        'login': True,
                                                        'team': team,
                                                        'date': date})
    else:
        return render_to_response('teamplay/teamplay.html',
                                 {'team': team,},
                                  context_instance=RequestContext(request))

def sign(request, userid):
    if 'name' in request.session:
        t = get_object_or_404(Team, id=userid)
        t.persons += request.session['name'] + ","
        t.save()
    return HttpResponseRedirect('/teamplay')

def sign_out(request, userid):
    if 'name' in request.session:
        t = get_object_or_404(Team, id=userid)
        name = request.session['name']
        t.persons = string.replace(t.persons, name+",", "")
        t.save()
    return HttpResponseRedirect('/teamplay')

def details(request, userid):
    name = ""
    user = ""
    login = False
    if 'email' and 'name' in request.session:
        name = request.session['name']
        user = request.session['email']
        login = True
    team = get_object_or_404(Team, id=userid)
    tab = team.persons.split(",")
    return render_to_response('detail.html', {'team': team,
                                              'name': name,
                                              'tab': tab,
                                              'user': user,
                                              'login': login})

def add_teamplay(request):
    if 'email' in request.session:
        if request.POST:
            team = Team(title=request.POST['title'], leader=request.session['name'], date=request.POST['date'])
            team.save()
            return HttpResponseRedirect('/teamplay')
        else:
            select = 1
            return render_to_response('teamplay/add_teamplay.html', {'user': request.session,
                                                             'login': True,
                                                             'edit': False,
                                                             'select': select})
    return HttpResponseRedirect('/')

def edit_teamplay(request, teamid):
    team = get_object_or_404(Team, id=teamid)
    if 'email' in request.session:
        if request.POST:
            team.title = request.POST['title']
            team.win = request.POST['win']
            team.draw = request.POST['draw']
            team.defeat = request.POST['defeat']
            team.save()
        else:
            select = 1
            if team.title in "7 vs 7":
                select = 1
            elif team.title in "Kompania VIII tieru":
                select = 2
            elif team.title in "Kompania VI tieru":
                select = 3
            elif team.title in "Kompania IV tieru":
                select = 4
            return render_to_response('teamplay/add_teamplay.html', {'user': request.session,
                                                          'login': True,
                                                          'team': team,
                                                          'edit': True,
                                                          'select': select})
    return HttpResponseRedirect('/teamplay')