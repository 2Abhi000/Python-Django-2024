from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
def homepage(request):
    data={
        'title':'Image Gallery',
        
    }
    return render(request,"index.html",data)

def table(request):
    data={
        'title':'Table',
        'stud' : [
            {'name':'Abhishek','phone':562753627},
            {'name':'Jay Sir','phone':5222753627},
            {'name':'Harsh Sir','phone':562733327},
            {'name':'Vikram','phone':5622253627}
            ]
    }
    return render(request,"table.html",data)

def slug(request,course):
    return HttpResponse(course)

def calcform(request):
    ad=0
    try:
        if request.method=="POST":
            n1=int(request.POST.get('v1'))
            n2=int(request.POST.get('v2'))
            ad=n1+n2
    except:
        pass
    return render(request,"calcform.html",{'op':ad})

def redirect(request):
    ad=0
    try:
        if request.method=="POST":
            n1=int(request.POST.get('v1'))
            n2=int(request.POST.get('v2'))
            ad=n1+n2
            url="/This/?output={}".format(ad)
            return HttpResponseRedirect(url)
        #another way = return HttpResponseRedirect('/This/')
    except:
        pass
    return render(request,"redirect.html",{'op':ad})

def This(request):
    data={
        'title':'This Page',
        
    }
    return render(request,"This.html",data)