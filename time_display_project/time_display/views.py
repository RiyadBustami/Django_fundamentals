from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.
def redirect_time(request):
    return redirect('/time_display')

def show_time(request):
    context={
        "time": strftime("%Y-%m-%d %H:%M %p")
    }
    return render(request, "index.html",context)