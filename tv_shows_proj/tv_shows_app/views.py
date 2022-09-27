from django.shortcuts import render,redirect,HttpResponse
from tv_shows_app.models import Show
from time import strftime
# Create your views here.
def new_show(request):
    return render(request,"new_show.html")
    # return HttpResponse("method should return a template containing the form for adding a new TV show")

def create_show(request):
    if request.method=='POST':
        last_show=Show.objects.create(title=request.POST['title']
                    ,network=request.POST['network']
                    ,release_date=request.POST['release_date']
                    ,desc=request.POST['desc'])
        return redirect("/shows/"+str(last_show.id)+"/")
    # return HttpResponse("- POST - method should add the show to the database, then redirect to /shows/<id>")

def display_show(request,id):
    context={
        "show":Show.objects.get(id=id),
    }
    return render(request,"display_show.html",context)
    # return HttpResponse("- GET - method should return a template that displays the specific show's information "+id)


def display_all_shows(request):
    context={
        "shows":Show.objects.all(),
    }
    return render(request,"shows.html",context)
    # return HttpResponse("- GET - method should return a template that displays all the shows in a table")


def edit_show(request,id):
    context={
        "show":Show.objects.get(id=id),
        "show_release_date":Show.objects.get(id=id).release_date.strftime('%Y-%m-%d'),
    }
    return render(request,"edit_show.html",context)
    # return HttpResponse("method should return a template that displays a form for editing the TV show with the id specified in the url "+id)


def update_show(request,id):
    show=Show.objects.get(id=id)
    if(request.method=='POST'):
        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.desc=request.POST['desc']
        show.save()
    
    return redirect("/shows/"+id+"/")


    # return HttpResponse(" - POST - method should update the specific show in the database, then redirect to /shows/<id> "+id)


def delete_show(request,id):
    deleted_to_be=Show.objects.get(id=id)
    deleted_to_be.delete()
    return redirect("/shows/")
    # return HttpResponse("- POST - method should delete the show with the specified id from the database, then redirect to /shows "+id)

def index(request):
    return redirect('/shows')