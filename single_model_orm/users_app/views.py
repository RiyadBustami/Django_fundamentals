from django.shortcuts import render,HttpResponse,redirect
from users_app.models import *

# Create your views here.
def index(request):
    
    
    context={
        "users_views":User.objects.all()
    }
    print(context)
        
    return render(request,"index.html",context)

def process(request):
    if(request.method == 'POST'):
        User.objects.create(first_name = request.POST["first_name"]
        ,last_name = request.POST["last_name"]
        ,email_address = request.POST["email"]
        ,age = request.POST["age"])
    return redirect('/')

def delete_rows(request):
    users=User.objects.all()
    users.delete()
    return redirect('/')