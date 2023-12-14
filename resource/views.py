from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 
from .models import * 

# Create your views here.

def index(request): 
    return render(request, "resource/index.html", { 
        "PostType": PT.objects.all(), 
        "Stamp": Quality.objects.all(), 
    }) 

def page(request, pageId): 
    return render(request, "resource/showposts.html", { 
        "t": Post.objects.filter(id__range=((pageId-1)*50,pageId*50-1)), 
        "p": pageId 
    })  

def search(request): 
    return HttpResponseRedirect(reverse("index")) 

def search(request, pt, st, name): 
    if (name == "ALL"): 
        name = "" 
    if (pt == 0 and st == 0): 
        answer = Post.objects.filter(title__icontains=(name)) 
    elif (pt == 0): 
        answer = Post.objects.filter(stamp=(Quality.objects.get(pk=st)), title__icontains=(name)) 
    elif (st == 0): 
        answer = Post.objects.filter(postType=(PT.objects.get(pk=pt)), title__icontains=(name)) 
    else: 
        answer = Post.objects.filter(postType=(PT.objects.get(pk=pt)), stamp=(Quality.objects.get(pk=st)), title__icontains=(name)) 
    return render(request, "resource/showposts.html", { 
        "t": answer, 
        "p": 1 
    }) 

def filter(request): 
    if request.method == "POST": 
        PostType = int(request.POST["Pt"]) 
        Stamp = int(request.POST["Quality"]) 
        Name = request.POST["name"] 
        if Name == "" : 
            Name = "ALL" 
        return HttpResponseRedirect(reverse("search", args=(PostType, Stamp, Name))) 
    return HttpResponseRedirect(reverse("index")) 
