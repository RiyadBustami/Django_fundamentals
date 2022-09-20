from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def result(request):
    if request.method == "POST":
        context={
            "name_on_page":request.POST['name'],
            "location_on_page": request.POST['location'],
            "fav_lang_on_page": request.POST['fav-lang'],
            "comment_on_page": request.POST['comment']
        }
        return render(request,'result.html',context)