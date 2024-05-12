from django.shortcuts import render,HttpResponseRedirect, get_object_or_404
from .forms import Studentdata
from django.http import HttpResponse
from .models import User


# This function will add and show data
def add_show(request):
    if request.method == "POST":
        fm = Studentdata(request.POST)
        if fm.is_valid():
            print(fm)
            fm.save()
            #return HttpResponse('success')
            fm = Studentdata()
    else:
        fm = Studentdata()
    
    stud = User.objects.all()     #for getting data from database
    return render(request , 'myapp/addandshow.html' , {'form':fm , 'stud':stud})

 
# This function will update data 
def update_data(request,id):
    if request.method == "POST":
        #pi = User.objects.get(pk=id)
        pi= get_object_or_404(User, id=id)
        fm = Studentdata(request.POST or None, instance=pi)
        print(pi)
        if fm.is_valid():
            fm.save()
    else:
        #pi = User.objects.get(pk=id)
        pi= get_object_or_404(User, id=id)
        #print(pi)
        fm = Studentdata(instance=pi)        
    return render(request , 'myapp/update.html' , {'form':fm , 'pi':pi})


# This function will delete data 
def delete_data(request,id):
    if request.method =="POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')