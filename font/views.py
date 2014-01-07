import random
from django.core.context_processors import csrf
from models import *
from django.shortcuts import *


def get_para(request):
    ret = {}
    for (k, v) in request.POST.items():
        ret[k] = v
    for (k, v) in request.GET.items():
        ret[k] = v
    return ret


def check_para(p, needs):
    error = ''
    for need in needs:
        if need not in p:
            error += need + ' is required! '
    return error


def handle_error(request, error):
    return render_to_response('error.html', {'error_info': error, 'back_url': request.path})


def view_register(request):
    return render_to_response('register.html', csrf(request))


def register_btn(request):
    p = get_para(request)
    print p
    error = check_para(p, ['username', 'password', 'email'])
    if error:
        return handle_error(request, error)

    if not p['username'] or not p['password']:
        return handle_error(request, 'invalid username or password')

    res = Users.objects.filter(username=p['username'])
    if res:
        return handle_error(request, 'duplicate username')

    user = Users.objects.create(
        username=p['username'],
        password=p['password'],
        email=p['email']
    )
    if not user:
        return handle_error(request, "can't create user! unknown reason")
    return HttpResponseRedirect('/login/')


def view_login(request):
    return render_to_response('login.html', csrf(request))


def login_btn(request):
    p = get_para(request)
    error = check_para(p, ['username', 'password'])
    if error:
        return handle_error(request, error)

    res = Users.objects.filter(username=p['username'])
    if not res or res[0].password != p['password']:
        resp = redirect('/login/')
        resp.set_cookie('login_error')
        return resp

    user = res[0]

    user.sid = random.randrange(1e9)
    user.last_login = datetime.datetime.now()
    user.save()

    resp = HttpResponseRedirect('/home/')
    resp.set_cookie('uid', user.id)
    resp.set_cookie('sid', user.sid)
    return resp


def logged(request):
    uid = request.COOKIES.get('uid')
    sid = request.COOKIES.get('sid')

    res = Users.objects.filter(id=uid)
    if not res:
        return False
    user = res[0]
    if sid != user.sid:
        return False

    return True


def view_home(request):
    if not logged(request):
        return handle_error(request, 'not logged in')

    return render_to_response('home.html', csrf(request))