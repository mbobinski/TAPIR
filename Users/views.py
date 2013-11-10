from django.shortcuts import render_to_response, get_object_or_404
from Users.models import JadeBusemUser
from forms import RegisterForm
from django.template import Context
from forms import SignInForm
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
import random


def register(request):
    email_error = ""
    password_error = ""

    if (request.method == 'POST'):
        password = request.POST['password']
        password2 = request.POST['password2']
        if (len(password) >= 6):
            if (password == password2):
                try:
                    user = JadeBusemUser.objects.create_user(request.POST['email'], password)
                    user.user_id = str(random.randint(999999, 9999999))
                    while(1):
                        try:
                            JadeBusemUser.objects.get(user_id=user.user_id)
                            user.user_id = str(random.randint(999999, 999999999))
                        except:
                            break;
                    user.name = request.POST['name']
                    user.message = request.POST['message']
                    user.is_rules_accepted = request.POST['rules']
                    user.save()
                    return render_to_response('user/thanks.html')
                except:
                    email_error = "Ten E-mail jest juz zajety"
            else:
                password_error = "Hasla nie sa identyczne"
        else:
            password_error = "Haslo musie skladac sie przynajmniej z 6 znakow"

    # if error than display form again but with filled fields and error
    if (email_error != "" or password_error != ""):
        f = RegisterForm()
        context = Context(
            {'form': f,
             'email': request.POST['email'],
             'name': request.POST['name'],
             'message': request.POST['message'],
             'email_error': email_error,
             'password_error': password_error,
            })
    else:
        # Create blank form - we get here only at first time
        f = RegisterForm()
        context = Context({'form': f})
    return render_to_response('user/registration.html', context)


def login(request):
    error = False
    if request.method == 'POST':
        form = SignInForm(request.POST)
        email_address = request.POST['email']
        password = request.POST['password']
        try:
            user = JadeBusemUser.objects.get(email=email_address)
        except JadeBusemUser.DoesNotExist:
            error = "Nie ma takiego konta"
        if error is False:
            if check_password(password, user.password):
                if user.is_active:
                    is_login = True
                    request.session['email'] = user.email
                    request.session['name'] = user.name
                    request.session['is_recruter'] = user.is_recruter
                    request.session['is_tactic'] = user.is_tactic
                    return render_to_response('news/index.html', {'user': request.session,
                                                             'login': True})
                else:
                    error = "Twoje konto nie jest aktywne, zapytaj o to dowodce"
                    return render_to_response('news/index.html', {'form': form, 'error': error})

            else:
                error = "Bledne haslo"
                return render_to_response('news/index.html', {'form': form, 'error': error})
        else:
            return render_to_response('news/index.html', {'form': form, 'error': error})
    else:
        if 'email' in request.session:
            return render_to_response('news/index.html', {'user': request.session['name'],
                                                     'login': True})
        else:
            form = SignInForm()
        return render(request, 'news/index.html', {'form': form, 'error': error})

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')

def user_panel(request, userid):
    u = get_object_or_404(JadeBusemUser, user_id=userid)
    email_error = ""
    password_error = ""
    confirm_error = ""
    success = ""
    if request.method == 'POST':    
        if(u.check_password(request.POST['confirm'])):
            password = request.POST['password']
            password2 = request.POST['password2']
            if(password == "" or len(password) >= 6):
                if(password == password2):
                    try:
                        u.email = request.POST['email']
                        u.first_name = request.POST['first_name']
                        u.last_name = request.POST['last_name']
                        u.address = request.POST['address']
                        u.company_name = request.POST['company_name']
                        u.save()
                        if(len(password) >= 6):
                            u.set_password(password)
                            u.save()
                        success = "Changes have been saved!"
                    except:
                        email_error = "This e-mail is already in use"
                else:
                    password_error = "Passwords do not match"
            else:
                password_error = "Password must be at least six characters long"
        else:
            confirm_error = "Password is incorrect"
            
    if(email_error != "" or password_error != "" or confirm_error != ""): 
        context = Context(
                          {
                            'email': request.POST['email'],
                            'first_name': request.POST['first_name'],
                            'last_name': request.POST['last_name'],
                            'address': request.POST['address'],
                            'company_name': request.POST['company_name'],
                            'email_error': email_error,
                            'password_error': password_error,
                            'confirm_error': confirm_error
                            })
    else:
        context = Context({
                           'email': u.email,
                           'first_name': u.first_name,
                           'last_name': u.last_name,
                            'address': u.address,
                            'company_name': u.company_name,
                            'success': success,
                            })
    return render_to_response('user/user_panel.html', context)

def about(request):
    return render(request, 'user/about.html')

def new_user(request):
    if 'email' in request.session:
        user = JadeBusemUser.objects.all()
        return render_to_response('user/show_new_users.html', {'user': request.session,
                                                               'users': user,
                                                               'login': True})

def new_user_add(request, userid):
    if 'email' in request.session:
        user = get_object_or_404(JadeBusemUser, user_id=userid)
        user.is_active = True
        user.save()
        return render_to_response('user/show_new_users.html', {'user': request.session,
                                                               'login': True})

def new_user_out(request, userid):
    if 'email' in request.session:
        user = get_object_or_404(JadeBusemUser, user_id=userid)
        user.points = -100
        user.save()
        return render_to_response('user/show_new_users.html', {'user': request.session,
                                                               'login': True})
