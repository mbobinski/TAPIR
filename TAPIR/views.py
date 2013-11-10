from django.shortcuts import render_to_response

def mumble(request):
    if 'email' in request.session:
            return render_to_response('mumble.html', {'user': request.session,
                                                      'login': True})
    else:
        return render_to_response('mumble.html',
                                  {'login': False})

def rules(request):
    if 'email' in request.session:
            return render_to_response('rules.html', {'user': request.session,
                                                     'login': True})
    else:
        return render_to_response('rules.html',
                                  {'login': False})

def programs(request):
    if 'email' in request.session:
            return render_to_response('programs.html', {'user': request.session,
                                                        'login': True})
    else:
        return render_to_response('programs.html',
                                 {'login': False})