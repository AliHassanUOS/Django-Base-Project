from django.shortcuts import render,HttpResponseRedirect
from .models import Student,User
from .forms import StudentForm

# Create your views here.



def home(request):
    

    res = User.objects.all()
    res = list(res)
    res = res[::-1]

    return render(request, "student/home.html", {"res":res})


def fun(request):

    if request.method == "POST":
        obj = StudentForm(request.POST)

        if obj.is_valid():
            nm = obj.cleaned_data["name"]
            em = obj.cleaned_data["email"]
            nu = obj.cleaned_data["number"]
            pa = obj.cleaned_data["password"]
            pa1 = obj.cleaned_data["password1"]
            us = User(name = nm, email = em, number = nu, password = pa, password1 = pa)
            us.save()
            return HttpResponseRedirect("/")
    else:
        obj = StudentForm()
    
    return render(request, "student/detail.html", {"obj": obj} )



def update(request,myid):
    print(myid)

    if request.method == "POST":
         
        userid = User.objects.get(pk=myid)

        stdid = StudentForm(request.POST, instance=userid)

        if stdid.is_valid():
            nm = stdid.cleaned_data["name"]
            em = stdid.cleaned_data["email"]
            nu = stdid.cleaned_data["number"]
            pa = stdid.cleaned_data["password"]
            pa1 = stdid.cleaned_data["password1"]
            us = User(name = nm, email = em, number = nu, password = pa, password1 = pa1)
            us.save()
            return HttpResponseRedirect("/")
        else:
            userid = User.request.get(pk=myid)
            stdid = StudentForm(request.POST, instance=userid)
        
        return render(request,"student/updateform.html", {"myid": myid})






















