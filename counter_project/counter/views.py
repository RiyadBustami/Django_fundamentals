from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if "counter" not in request.session:
        request.session["counter"]=0
        request.session.save()
    request.session["counter"]+=1
    request.session.save()
    
    return render(request,"index.html")

def reset_session(request):
    del request.session['counter']
    return redirect('/')