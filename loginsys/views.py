from django.shortcuts import render
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from catalog.models import Cart
from  django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['visit'] = True
            return redirect('/')
        else:
            args['login_error'] = "User does not exist"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    request.session['visit'] = False
    return redirect('/')


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            request.session['visit'] = True
            cart = Cart()
            cart.owner = newuser
            cart.save()
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)
