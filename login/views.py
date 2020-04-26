from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def input(request):
    print('*'*100)
    print ('HOMEPAGE LOADING')
    print('*'*100)
    if 'user' not in request.session:
        request.session['user']={}
    return render (request,'login.html')

def register(request):
    print('*'*100)
    print('REGISTER LOADING')
    print(request.POST)
    # ------------------CLEAN DATA -------------------
    all_users=User.objects.all()
    errors= User.objects.cleandata_reg(request.POST)
    print(errors)
    if errors:
        for k,v in errors.items():
            messages.error(request,v,extra_tags=f'{k}')
        print("######################")
        print(messages)
        return redirect('/')
    # ------------------------------------------------
    else:
        a=request.POST['f_name']
        b=request.POST['l_name']
        c=request.POST['email']
        d=request.POST['pw']
        hashed_pw= bcrypt.hashpw(d.encode(),bcrypt.gensalt()).decode()
        User.objects.create(f_name=a,l_name=b,email=c,pw=hashed_pw)
        new_user=User.objects.get(email=c)
        request.session['user']={
            'f_name': a,
            'l_name': b,
            'id': new_user.id,
        }
        print('*'*100)
        return redirect('/success')
def login(request):
    print('*'*100)
    print('LOGIN LOADING')
    print(request.POST)
    # ------------------CLEAN DATA -------------------
    errors= User.objects.cleandata_log(request.POST)
    print(errors)
    if errors:
        for k,v in errors.items():
            messages.error(request,v,extra_tags=f'{k}')
        print("######################")
        print(messages)
        return redirect('/')
    # ------------------------------------------------
    else:
        a=request.POST['l_email']
        b=request.POST['l_pw']
        selected_user= User.objects.get(email=a)
        request.session['user']={
            'f_name': selected_user.f_name,
            'l_name': selected_user.l_name,
            'id': selected_user.id,
            }
        return redirect('/wall')

def success(request):
    print('*'*100)
    print('SUCCESS LOADING')
    print('*'*100)
    return render (request,'success.html')

def log_out(request):
    print('*'*100)
    print('LOG OUT LOADING')
    request.session.clear()
    print('*'*100)
    return redirect('/')
# Create your views here.
