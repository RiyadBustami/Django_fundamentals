from django.shortcuts import render,redirect
from dojo_ninjas_app.models import Ninja,Dojo

# Create your views here.
def index(request):

    context={
        "dojos":Dojo.objects.all().order_by('name'),
        "ninjas":Ninja.objects.all().order_by('first_name'),
        }
    print(context)
    return render(request,"index.html",context)


def add_dojo(request):
    if request.method == "POST":
        dojo_name=request.POST['dojo_name']
        dojo_city=request.POST['dojo_city']
        dojo_state=request.POST['dojo_state']
        Dojo.objects.create(name=dojo_name,city=dojo_city,state=dojo_state)
    return redirect("/")

def add_ninja(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dojo_id=request.POST['dojo']
        Ninja.objects.create(dojo=Dojo.objects.get(id=dojo_id),first_name=first_name,last_name=last_name)
    return redirect("/")