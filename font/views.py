from models import *
from django.shortcuts import *


def get_para(request):
    ret = {}
    for (k,v) in request.POST.items():
        ret[k] = v
    for (k,v) in request.GET.items():
        ret[k] = v
    return ret


def check_para(p, needs):
    error = ''
    for need in needs:
        if need not in p:
            error += need + ' is required! '
    return error


def handle_error(request, error):
    return render_to_response('error.html', {'error_info':error, 'back_url':request.path})


def register_btn(request):
    p = get_para(request)
    error = check_para(p, ['username', 'password', 'email'])
    if error:
        return handle_error(request, error)

    res = Users.objects.filter(username=p['username'])
    if res:
        return handle_error(request, 'duplicate username')

    user = Users.objects.create(
        username = p['username'],
        password = p['password'],
        email = p['email'],
        is_active = False
    )
    if not user:
        return handle_error(request, "can't create user! unknown reason")
    return HttpResponseRedirect('/login/')


def login_btn(request):
    p = get_para(request)
    error = check_para(p, ['username', 'password'])
    if error:
        return handle_error(request, error)
