from django.http import *


def get_para(request):
    ret = {}
    for (k,v) in request.POST.items():
        ret[k] = v
    for (k,v) in request.GET.items():
        ret[k] = v
    return ret


def check_para(p, needs):
    ret = ''
    for need in needs:
        if need not in p:
            ret += need + ' is required! '
    return ret


def handle_error(error):
    


def view_register(request):
    p = get_para(request)
    error = check_para(p, ['username', 'password'])
    if error:
        return handle_error(error)