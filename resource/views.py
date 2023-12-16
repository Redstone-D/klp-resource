from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 
from .models import * 

# Create your views here.

def index(request): 
    return render(request, "resource/index.html", { 
        "PostType": PT.objects.all(), 
        "Stamp": Quality.objects.all(), 
        "Version": Version.objects.all(), 
        "Originality": Originality.objects.all(), 
    }) 

def page(request, pageId): 
    return render(request, "resource/showposts.html", { 
        "t": Post.objects.filter(id__range=((pageId-1)*50,pageId*50-1)), 
        "p": pageId 
    })  

def search(request): 
    return HttpResponseRedirect(reverse("index")) 

def search(request, pt, st, vt, ori, name): 

    ptList = [0] * PT.__itemsize__ 
    stList = [0] * Quality.__itemsize__ 
    vtList = [0] * Version.__itemsize__ 
    oriList = [0] * Originality.__itemsize__ 
    nameList = [" "] * 30  

    if (pt == "ALL" or pt[0] == "0"): 
        ptList = list(PT.objects.values_list('pk', flat=True)) # get a list of primary keys of all the PT objects
    else: 
        try: 
            ptList = list(map(int, pt[:-1].split(","))) # split the string by comma and convert to integers
        except ValueError: # catch the ValueError exception 
            print(ValueError) 
            return HttpResponseRedirect(reverse("index")) 
    if (st == "ALL" or st[0] == "0"): 
        stList = list(Quality.objects.values_list('pk', flat=True)) # get a list of primary keys of all the Quality objects
    else: 
        try: 
            stList = list(map(int, st[:-1].split(","))) # split the string by comma and convert to integers
        except ValueError: # catch the ValueError exception 
            return HttpResponseRedirect(reverse("index")) 
    if (vt == "ALL" or vt[0] == "0"): 
        vtList = list(Version.objects.values_list('pk', flat=True)) # get a list of primary keys of all the Quality objects
    else: 
        try: 
            vtList = list(map(int, vt[:-1].split(","))) # split the string by comma and convert to integers
        except ValueError: # catch the ValueError exception 
            return HttpResponseRedirect(reverse("index")) 
    if (ori == "ALL" or ori[0] == "0"): 
        oriList = list(Originality.objects.values_list('pk', flat=True)) # get a list of primary keys of all the Quality objects
    else: 
        try: 
            oriList = list(map(int, ori[:-1].split(","))) # split the string by comma and convert to integers
        except ValueError: # catch the ValueError exception 
            return HttpResponseRedirect(reverse("index")) 
    if (name != "ALL"): 
        nameList = list(map(str, name.split(" "))) # split the string by space and convert to strings
        answer = Post.objects.filter(postType__in=PT.objects.filter(pk__in=ptList), stamp__in=Quality.objects.filter(pk__in=stList), ver__in=Version.objects.filter(pk__in=vtList), ori__in=Originality.objects.filter(pk__in=oriList), title__in=nameList) # search 
    else: 
        nameList = [""] 
        # print(vtList) 
        answer = Post.objects.filter(postType__in=PT.objects.filter(pk__in=ptList), stamp__in=Quality.objects.filter(pk__in=stList), ver__in=Version.objects.filter(pk__in=vtList), ori__in=Originality.objects.filter(pk__in=oriList)) # search 
    answer = answer.distinct() 
    
    '''       
    if (pt == 0 and st == 0): 
        answer = Post.objects.filter(title__icontains=(name)) 
    elif (pt == 0): 
        answer = Post.objects.filter(stamp=(Quality.objects.get(pk=st)), title__icontains=(name)) 
    elif (st == 0): 
        answer = Post.objects.filter(postType=(PT.objects.get(pk=pt)), title__icontains=(name)) 
    else: 
        answer = Post.objects.filter(postType=(PT.objects.get(pk=pt)), stamp=(Quality.objects.get(pk=st)), title__icontains=(name)) 
    ''' 
    
    return render(request, "resource/showposts.html", { 
        "t": answer, 
        "p": 1 
    }) 

def filter(request): 
    if request.method == "POST": 
        PostType = request.POST.getlist("Pt") 
        PostTypeList = "" 
        for temp in PostType: 
            PostTypeList += temp + "," 
        Stamp = request.POST.getlist("Quality") 
        StampList = "" 
        for temp in Stamp: 
            StampList += temp + "," 
        Ver = request.POST.getlist("Version") 
        VerList = "" 
        for temp in Ver: 
            VerList += temp + ","
        Ori = request.POST.getlist("Ori") 
        OriList = "" 
        for temp in Ori: 
            OriList += temp + "," 
        Name = request.POST["name"] 

        #If no data is inputted add all into it 
        if PostTypeList == "": 
            PostTypeList += "ALL"
        if StampList == "": 
            StampList += "ALL" 
        if VerList == "" : 
            VerList = "ALL" 
        if OriList == "" : 
            OriList = "ALL" 
        if Name == "" : 
            Name = "ALL" 
        return HttpResponseRedirect(reverse("search", args=(PostTypeList, StampList, VerList, OriList, Name))) 
        
    return HttpResponseRedirect(reverse("index")) 
