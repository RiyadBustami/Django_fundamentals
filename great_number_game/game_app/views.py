from re import sub
from django.shortcuts import render,HttpResponse,redirect
from random import randint

# Create your views here.
def index(request):
    if "rand" not in request.session:
        request.session['rand']=randint(1,100)
        request.session['flag']='init'

    print(request.session['rand'])
    return render(request, "index.html")


def do_the_math(request):
    original=int(request.session['rand'])
    sub_num=int(request.POST['number'])
    request.session['flag']='sub'

    if sub_num<original:
        request.session['status']='Too low!'
        request.session['card_color']='danger'

    elif sub_num==original:
        request.session['status']=str(request.session['rand'])+' is the right number!'
        request.session['card_color']='success'
        request.session['flag']='win'

    elif sub_num>original:
        request.session['status']='Too high!'
        request.session['card_color']='danger'
    status=request.session['status']
    print(original)
    print(sub_num)
    print(status)
    return redirect('/')


def celebrate(request):
    del request.session['status']
    del request.session['card_color']
    del request.session['flag']
    del request.session['rand']
    return redirect('/')