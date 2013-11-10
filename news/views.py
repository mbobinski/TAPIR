# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect, get_object_or_404
from news.models import News

def index(request):
    news = News.objects.all().order_by('-posted_date')
    if 'email' in request.session:
            return render_to_response('news/index.html', {'user': request.session,
                                                          'login': True,
                                                          'news': news})
    else:
        return render_to_response('news/index.html',
                                 {'news': news},
                                  context_instance=RequestContext(request))

def add_post(request):
    if 'email' in request.session:
        if request.POST:
            news = News(title=request.POST['title'], publicator=request.session['name'], text=request.POST['message'])
            news.save()
        else:
            return render_to_response('news/add_post.html', {'user': request.session,
                                                             'login': True,
                                                             'edit': False})
    return HttpResponseRedirect('/')

def edit_post(request, postid):
    news = get_object_or_404(News, id=postid)
    if 'email' in request.session:
        if request.POST:
            news.title = request.POST['title']
            news.publicator = request.session['name']
            news.text = request.POST['message']
            news.save()
        else:
            return render_to_response('news/add_post.html', {'user': request.session,
                                                          'login': True,
                                                          'title': news.title,
                                                          'message': news.text,
                                                          'edit': True,
                                                          'id': news.id})
    return HttpResponseRedirect('/')