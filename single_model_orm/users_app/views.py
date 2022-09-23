from django.shortcuts import render,HttpResponse,redirect
from users_app.models import *

# Create your views here.
def index(request):
    users_views=User.objects.all()
    
    context={
        "users_in_context":[]
    }

    for user in users_views:
        temp=[]
        temp.append(user.id)
        temp.append(user.first_name+' '+user.last_name)
        temp.append(user.email_address)
        temp.append(user.age)
        context['users_in_context'].append(temp)
        

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