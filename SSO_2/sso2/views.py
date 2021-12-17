from django.http import HttpResponse
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        user = request.POST['usr']
        password = request.POST['password']
        request.session['usr'] = user
        request.session['password'] = password
        return HttpResponse(
            "usr:{},password:{},sessionid:{},cookie:{}".format(user, password,
                                                               request.session.session_key, request.COOKIES)
        )
    else:
        if 'usr' in request.session:
            user = request.session['usr']
            password = request.session['password']
            return HttpResponse(
                "usr:{},password:{},sessionid:{},cookie:{}".format(user, password, request.session.session_key,
                                                                   request.COOKIES)
            )
        return render(request, 'login.html')


def logout(request):
    request.session.clear()
    return redirect('/login')
