from django.shortcuts import render, redirect
from .models import User

def index(request):
    return render(request, "user_valid/index.html")

def start(request):
    return redirect('/')

def submit(request):
    result = User.objects.validate(request.POST['name'])
    if 'succes' in result:
        request.session['message'] = result['succes']
        return redirect('/succes')
    if 'error' in result:
        context = {
            'message':result['error']
        }
    return render(request, 'user_valid/index.html', context)

def succes(request):
    context = {
        'message':request.session['message'],
        'list':User.objects.show_all()
    }
    return render(request, 'user_valid/succes.html', context)

def delete(request, id):
    User.objects.remove(id)
    return redirect('/succes')
