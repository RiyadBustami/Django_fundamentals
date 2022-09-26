from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/blogs")

def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request,number):
    return redirect("/blogs")

def json_response(request):
    context={
        "title":'My first blog',
        'content':"Lorem, ipsum dolor sit amet consectetur adipisicing elit."
            }
    return JsonResponse(context)